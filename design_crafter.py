# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_crafter2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(327, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/HAL-9000.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QToolButton {\n"
"background -color: transparent;\n"
"border: none;\n"
"}\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color:rgb(193, 210, 238);\n"
"border: 1px solid rgb(60, 127, 177);\n"
"}\n"
"QToolButton:hover {\n"
"background-color: rgb(224, 232, 245);\n"
"}\n"
"QToolButton:checked:hover {\n"
"background-color:rgb(193, 210, 238);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.arp_tab = QtGui.QWidget()
        self.arp_tab.setStyleSheet(_fromUtf8(""))
        self.arp_tab.setObjectName(_fromUtf8("arp_tab"))
        self.gridLayout = QtGui.QGridLayout(self.arp_tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gateway_label = QtGui.QLabel(self.arp_tab)
        self.gateway_label.setObjectName(_fromUtf8("gateway_label"))
        self.gridLayout.addWidget(self.gateway_label, 8, 0, 1, 2)
        self.gateway_mac_box = QtGui.QLineEdit(self.arp_tab)
        self.gateway_mac_box.setObjectName(_fromUtf8("gateway_mac_box"))
        self.gridLayout.addWidget(self.gateway_mac_box, 9, 0, 1, 3)
        self.source_ip_box = QtGui.QLineEdit(self.arp_tab)
        self.source_ip_box.setObjectName(_fromUtf8("source_ip_box"))
        self.gridLayout.addWidget(self.source_ip_box, 5, 3, 1, 2)
        self.hardware_length_box = QtGui.QLineEdit(self.arp_tab)
        self.hardware_length_box.setObjectName(_fromUtf8("hardware_length_box"))
        self.gridLayout.addWidget(self.hardware_length_box, 12, 0, 1, 1)
        self.mitm_box = QtGui.QCheckBox(self.arp_tab)
        self.mitm_box.setObjectName(_fromUtf8("mitm_box"))
        self.gridLayout.addWidget(self.mitm_box, 14, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(7, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 14, 1, 1, 1)
        self.stop_arp_button = QtGui.QPushButton(self.arp_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/Delete_48x48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_arp_button.setIcon(icon1)
        self.stop_arp_button.setObjectName(_fromUtf8("stop_arp_button"))
        self.gridLayout.addWidget(self.stop_arp_button, 14, 2, 1, 2)
        self.send_arp_button = QtGui.QPushButton(self.arp_tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/Check_48x48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_arp_button.setIcon(icon2)
        self.send_arp_button.setObjectName(_fromUtf8("send_arp_button"))
        self.gridLayout.addWidget(self.send_arp_button, 14, 4, 1, 1)
        self.target_label = QtGui.QLabel(self.arp_tab)
        self.target_label.setObjectName(_fromUtf8("target_label"))
        self.gridLayout.addWidget(self.target_label, 6, 0, 1, 2)
        self.target_ip_box = QtGui.QLineEdit(self.arp_tab)
        self.target_ip_box.setObjectName(_fromUtf8("target_ip_box"))
        self.gridLayout.addWidget(self.target_ip_box, 7, 3, 1, 2)
        self.hardware_type_box = QtGui.QLineEdit(self.arp_tab)
        self.hardware_type_box.setObjectName(_fromUtf8("hardware_type_box"))
        self.gridLayout.addWidget(self.hardware_type_box, 11, 0, 1, 1)
        self.source_label = QtGui.QLabel(self.arp_tab)
        self.source_label.setObjectName(_fromUtf8("source_label"))
        self.gridLayout.addWidget(self.source_label, 4, 0, 1, 2)
        self.protocol_length_box = QtGui.QLineEdit(self.arp_tab)
        self.protocol_length_box.setText(_fromUtf8(""))
        self.protocol_length_box.setObjectName(_fromUtf8("protocol_length_box"))
        self.gridLayout.addWidget(self.protocol_length_box, 13, 0, 1, 1)
        self.advanced_label = QtGui.QLabel(self.arp_tab)
        self.advanced_label.setObjectName(_fromUtf8("advanced_label"))
        self.gridLayout.addWidget(self.advanced_label, 10, 0, 1, 3)
        self.source_mac_box = QtGui.QLineEdit(self.arp_tab)
        self.source_mac_box.setObjectName(_fromUtf8("source_mac_box"))
        self.gridLayout.addWidget(self.source_mac_box, 5, 0, 1, 3)
        self.protocol_type_box = QtGui.QLineEdit(self.arp_tab)
        self.protocol_type_box.setObjectName(_fromUtf8("protocol_type_box"))
        self.gridLayout.addWidget(self.protocol_type_box, 12, 4, 1, 1)
        self.operation_box = QtGui.QLineEdit(self.arp_tab)
        self.operation_box.setObjectName(_fromUtf8("operation_box"))
        self.gridLayout.addWidget(self.operation_box, 13, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(127, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 4, 1, 1)
        self.target_mac_box = QtGui.QLineEdit(self.arp_tab)
        self.target_mac_box.setObjectName(_fromUtf8("target_mac_box"))
        self.gridLayout.addWidget(self.target_mac_box, 7, 0, 1, 3)
        self.gateway_ip_box = QtGui.QLineEdit(self.arp_tab)
        self.gateway_ip_box.setObjectName(_fromUtf8("gateway_ip_box"))
        self.gridLayout.addWidget(self.gateway_ip_box, 9, 3, 1, 2)
        self.interface_box = QtGui.QComboBox(self.arp_tab)
        self.interface_box.setObjectName(_fromUtf8("interface_box"))
        self.gridLayout.addWidget(self.interface_box, 4, 4, 1, 1)
        self.tabWidget.addTab(self.arp_tab, _fromUtf8(""))
        self.tcp_tab = QtGui.QWidget()
        self.tcp_tab.setObjectName(_fromUtf8("tcp_tab"))
        self.tabWidget.addTab(self.tcp_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.gateway_label.setBuddy(self.gateway_mac_box)
        self.target_label.setBuddy(self.target_mac_box)
        self.source_label.setBuddy(self.source_mac_box)
        self.advanced_label.setBuddy(self.hardware_type_box)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packet Crafter", None))
        self.arp_tab.setToolTip(_translate("MainWindow", "ARP packet forger", None))
        self.arp_tab.setStatusTip(_translate("MainWindow", "ARP", None))
        self.arp_tab.setWhatsThis(_translate("MainWindow", "ARP whatsthis", None))
        self.arp_tab.setAccessibleName(_translate("MainWindow", "accessible", None))
        self.arp_tab.setAccessibleDescription(_translate("MainWindow", "accessibledesc", None))
        self.gateway_label.setText(_translate("MainWindow", "Gateway:", None))
        self.gateway_mac_box.setToolTip(_translate("MainWindow", "Only specify a gateway if you want to do an MitM attack. Not required for normal queries.", None))
        self.gateway_mac_box.setPlaceholderText(_translate("MainWindow", "Gateway MAC", None))
        self.source_ip_box.setToolTip(_translate("MainWindow", "Internetwork address of the sender.", None))
        self.source_ip_box.setStatusTip(_translate("MainWindow", "SPA", None))
        self.source_ip_box.setPlaceholderText(_translate("MainWindow", "Source IP", None))
        self.hardware_length_box.setToolTip(_translate("MainWindow", "Length (in octets) of a hardware address. Ethernet addresses size is 6.", None))
        self.hardware_length_box.setStatusTip(_translate("MainWindow", "HLEN", None))
        self.hardware_length_box.setPlaceholderText(_translate("MainWindow", "0x06", None))
        self.mitm_box.setToolTip(_translate("MainWindow", "Enable MitM mode (Sending infinite gratuitous ARP replies)", None))
        self.mitm_box.setText(_translate("MainWindow", "MitM", None))
        self.stop_arp_button.setText(_translate("MainWindow", "Stop", None))
        self.send_arp_button.setToolTip(_translate("MainWindow", "Send!", None))
        self.send_arp_button.setStatusTip(_translate("MainWindow", "Send the packet", None))
        self.send_arp_button.setText(_translate("MainWindow", "Send", None))
        self.target_label.setText(_translate("MainWindow", "Target addresses:", None))
        self.target_ip_box.setToolTip(_translate("MainWindow", "Internetwork address of the intended receiver.", None))
        self.target_ip_box.setStatusTip(_translate("MainWindow", "TPA", None))
        self.target_ip_box.setPlaceholderText(_translate("MainWindow", "Target IP", None))
        self.hardware_type_box.setToolTip(_translate("MainWindow", "Hardware Type (HTYPE). Ethernet is 1.", None))
        self.hardware_type_box.setStatusTip(_translate("MainWindow", "HTYPE", None))
        self.hardware_type_box.setPlaceholderText(_translate("MainWindow", "0x0001", None))
        self.source_label.setText(_translate("MainWindow", "Source Addresses:", None))
        self.protocol_length_box.setToolTip(_translate("MainWindow", "Length (in octets) of addresses used in the upper layer protocol. (The upper layer protocol specified in PTYPE.) IPv4 address size is 4.", None))
        self.protocol_length_box.setStatusTip(_translate("MainWindow", "PLEN", None))
        self.protocol_length_box.setPlaceholderText(_translate("MainWindow", "0x04", None))
        self.advanced_label.setText(_translate("MainWindow", "Advanced options:", None))
        self.source_mac_box.setToolTip(_translate("MainWindow", "Media address of the sender. (E.g. MAC address)", None))
        self.source_mac_box.setStatusTip(_translate("MainWindow", "SHA", None))
        self.source_mac_box.setPlaceholderText(_translate("MainWindow", "Source MAC", None))
        self.protocol_type_box.setToolTip(_translate("MainWindow", "Internet protocol. IPv4 = 0x0800", None))
        self.protocol_type_box.setStatusTip(_translate("MainWindow", "PTYPE", None))
        self.protocol_type_box.setPlaceholderText(_translate("MainWindow", "0x0800", None))
        self.operation_box.setToolTip(_translate("MainWindow", "Specifies the operation that the sender is performing: 1 for request, 2 for reply.", None))
        self.operation_box.setStatusTip(_translate("MainWindow", "OPER", None))
        self.operation_box.setPlaceholderText(_translate("MainWindow", "0x0001", None))
        self.target_mac_box.setToolTip(_translate("MainWindow", "Media address of the intended receiver. In an ARP request this field is ignored. In an ARP reply this field is used to indicate the address of the host that originated the ARP request.", None))
        self.target_mac_box.setStatusTip(_translate("MainWindow", "THA", None))
        self.target_mac_box.setPlaceholderText(_translate("MainWindow", "Target MAC", None))
        self.gateway_ip_box.setPlaceholderText(_translate("MainWindow", "Gateway IP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arp_tab), _translate("MainWindow", "ARP", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.arp_tab), _translate("MainWindow", "ARP packet forger", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tcp_tab), _translate("MainWindow", "TCP", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))

