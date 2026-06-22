#/usr/bin/env python
import signal
import sys
import sys
import signal
from utils import (
	enable_port_forwarding,
	set_iptables,
	start_bettercap,
	disable_port_forwarding,
	clear_iptables
)

# What do we want to do when we hear a CTRL+C
def signal_handler(signal, frame):
    print("\n[-] Ctrl-C detected. Shutting down... ")
    # 1. shutdown port forwarding
    disable_port_forwarding.disable_port_forwarding()
    # 2. flush iptables
    clear_iptables.clear_iptables()
    # 3. Better cap can manage itself
    sys.exit(0)

try:
	print("[+] Setting up environment...")
	print("[+] Just a head's up, this script is for use with Linux only: ")
	# 1. Enable Port Forwarding.
	enable_port_forwarding.enable_port_forwarding()
	# 2. Set IP Tables
	set_iptables.set_iptables()
	# 3. Start Bettercap
	start_bettercap.start_bettercap()

except Exception as e:
	print("[-] Something went wrong while setting up environment: ", e)

# Register the handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Keeps the script running until a signal is received
signal.pause()