#/usr/bin/env python
# Rebuild
import scapy.all as scapy
from scapy.layers import http

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

