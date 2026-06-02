#/usr/bin/env python
# sniff for urls in packet
import scapy.all as scapy
from scapy.layers import http

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

