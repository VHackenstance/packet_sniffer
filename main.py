#/usr/bin/env python

from utils.packet_sniffer_utils import sniff, process_sniffed_packet

if __name__ == "__main__":
    sniff("eth0", process_sniffed_packet)
