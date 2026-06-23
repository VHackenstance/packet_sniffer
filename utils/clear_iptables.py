#/usr/bin/env python
import subprocess

def clear_iptables():
	yes_choice = {'yes', 'y'}
	no_choice = {'no', 'n'}

	print("[+] Flushing iptables...")
	user_input = input("[+] IP Tables will be cleared? y/n ").lower().strip()
	if user_input in yes_choice:
		subprocess.call(["sudo", "iptables", "--flush"])
	if user_input in no_choice:
		print("[+] Do nothing leave IP Tables.")
		exit()
	print("[+] Check IP Tables have been cleared.")
	subprocess.call(["sudo", "iptables", "-L"])













