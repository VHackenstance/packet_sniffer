#/usr/bin/env python
import scapy.all as scapy

if __name__ == "__packet_sniffer__":
    print("packet_sniffer is being called")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="udp")

def process_sniffed_packet(packet):
    print(packet)

sniff("eth0")
