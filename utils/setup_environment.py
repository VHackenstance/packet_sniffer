#/usr/bin/env python
import subprocess
# Required as DEVNULL only added to subprocess from V3.3
try:
	from subprocess import DEVNULL
except ImportError:
	import os
	DEVNULL = open(os.devnull, 'wb')


# SET UP THE EXPLOIT ENVIRONMENT
# With a single script we want to

# A. On ENTRY.
	# 1. Enable port forwarding.
		# a. Bug: cat /proc/sys/net/ipv4/ip_forward return 1,
		# just enable regardless
print("[+] Setting up environment...")
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
	# 2. Set iptables
		# a. I now realize  it is easier just to set ALL the iptables
		# b. Set default channel 0 but allow user to specify another
	# 3. Start ARP Spoof, if required for remote testing, again check
	# 4. Call SSLStrip using Bettercap

# B. On EXIT
	# 1. Disable port forwarding
	# 2. Flush iptables
	# 3. Shutdown ARP Spoof
	# 4. Shutdown Bettercap
	# 5. Say bye bye and laters
