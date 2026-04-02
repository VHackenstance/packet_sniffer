#/usr/bin/env python

from scapy.all import sniff

def process_sniffed_packet(packet):
    print(packet)

def sniff_interface(interface):
    # sniff Arguments:
    # store=False: tells scapy not to store the packets in memory.
    # prn=[CALL_BACK_FUNCTION]:
    sniff(iface=interface, store=False, prn=process_sniffed_packet)

# Not going to go ON_PATH here. Not going to use arp_spoofer.
# while building the script it is easier to test it on my own computer.
sniff_interface("eth0")