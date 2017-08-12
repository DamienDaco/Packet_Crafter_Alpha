import netifaces
import subprocess
import sys
import re

'''
def get_mac(interface):

  try:
    mac = open('/sys/class/net/'+interface+'/address').readline()
  except:
    mac = "00:00:00:00:00:00"

  return mac[0:17]
'''
'''
Excellent:
https://stackoverflow.com/questions/30698521/python-netifaces-how-to-get-currently-used-network-interface
'''


def get_default_interface():
    #Let's get our default interface, by getting the device used by the default IPv4 route.
    default_interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    return default_interface


def get_mac(interface):

    addrs = netifaces.ifaddresses(interface)
    mac = addrs[netifaces.AF_LINK][0]['addr']
    return mac


def get_host_ip(interface):
    ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    return ip


def get_gateway():

    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    return gateway


def get_interfaces():

    interface_list = netifaces.interfaces()
    return interface_list

#from https://www.ibm.com/developerworks/aix/library/au-pythocli/
def arping(device, ip):
    """Arping function takes IP Address or Network, returns nested mac/ip list"""

    # Assuming use of arping on Red Hat Linux
    p = subprocess.Popen("arping -c 1 -I %s %s" % (device, ip), shell=True,
                         stdout=subprocess.PIPE)
    out = p.stdout.read()
    result = out.split()
    pattern = re.compile(":")
    for item in result:
        if re.search(pattern, item):
            mac = item[1:18]
            return mac


#Found at https://stackoverflow.com/questions/2010816/get-remote-mac-address-using-python-and-linux
def get_remote_mac(ip):

    cmd = "arp -n"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, errors = p.communicate()

    if output is not None:
        output = output.decode('ascii')
        if sys.platform in ['linux', 'linux2']:
            for i in output.split("\n"):
                if ip in i:
                    for j in i.split():
                        if ":" in j:
                            return j
        # elif sys.platform in ['win32']:
        #     item = output.split("\n")[-2]
        #     if ip in item:
        #         print("%s-->  %s" % (ip, item.split()[1]))
