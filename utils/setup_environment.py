#/usr/bin/env python



# SET UP THE EXPLOIT ENVIRONMENT
# With a single script we want to

# A. On ENTRY.
	# 1. Enable port forwarding.
		# a. I don't think we need check but it might be fun to do so
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
