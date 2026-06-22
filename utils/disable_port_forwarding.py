#/usr/bin/env python
import subprocess
try:
	from subprocess import DEVNULL
except ImportError:
	import os
	# pylint: disable-msg=C0103
	DEVNULL = open(os.devnull, 'wb')

def disable_port_forwarding():
	print("[+] Disabling port forwarding. ")
	subprocess.call(
		"echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward",
		shell=True,
		stdout=DEVNULL
	)

	with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
		value = f.read().strip()
		if value == "0":
			print("[+] Port Forwarding disabled. Bye bye keep smiling.")
		else:
			print("[+] Something went wrong.  Manually disable.")