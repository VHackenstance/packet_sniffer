#/usr/bin/env python
# sniff for urls in packet
import scapy.all as scapy
from scapy.layers import http

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Requeset for URL: " + url)

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

