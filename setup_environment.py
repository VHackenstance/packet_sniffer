#/usr/bin/env python
from utils import (
	enable_port_forwarding,
	set_iptables,
	start_bettercap,
	disable_port_forwarding,
	clear_iptables
)

try:
	print("[+] Setting up environment...")
	print("[+] Just a head's up, this script is for use with Linux only: ")
	# 1. Enable Port Forwarding.
	enable_port_forwarding.enable_port_forwarding()
	# 2. Set IP Tables
	# set_iptables.set_iptables()
	# 3. Start Bettercap
	# start_bettercap.start_bettercap()

except Exception as e:
	print("[-] Something went wrong while setting up environment: ", e)
except KeyboardInterrupt:
	print("\n[-] Ctrl-C detected. Shutting down... ")
	# 1. shutdown port forwarding
	disable_port_forwarding.disable_port_forwarding()
	# 2. flush iptables
	clear_iptables.clear_iptables()
	# 3. Better cap can manage itself
