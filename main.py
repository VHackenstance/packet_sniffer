#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    # sniff(er) Arguments:
    # store=False: tells scapy not to store the packets in memory.
    # prn=[CALL_BACK_FUNCTION]:
    # filter="": tcp, udp, port#, arp,
    # We want to filter http packets, so for this we need a third party module
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

# Not going to go ON_PATH here = use arp_spoofer.
# while building script it is easier to test it on my HOST.
if __name__ == "__main__":
    sniff("lo")