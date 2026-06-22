#/usr/bin/env python
import subprocess

def set_iptables():
	number = None
	yes_choice = {'yes', 'y'}
	no_choice = {'no', 'n'}

	print("[+] Setting iptables...")
	user_input = input("[+] Queue number is 0. Is this acceptable? y/n  ").lower().strip()
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