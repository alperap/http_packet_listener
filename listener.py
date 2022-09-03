from optparse import OptionParser
import scapy.all as scapy
from scapy_http import http

def user_inputs():
    option = OptionParser()
    option.add_option("-i","--interface",dest="Interface",help="This is your interface name")
    output = option.parse_args()[0]

    if output.Interface:
        return output
    else:
        print("You have to enter your interface!")


def call_func(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


def listen(iface):
    scapy.sniff(iface=iface, store=False, prn=call_func)

h = user_inputs()

listen(h.Interface)


