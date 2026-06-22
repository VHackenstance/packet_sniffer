#/usr/bin/env python
import subprocess
try:
	from subprocess import DEVNULL
except ImportError:
	import os
	# pylint: disable-msg=C0103
	DEVNULL = open(os.devnull, 'wb')

def enable_port_forwarding():
    yes_choice = {'yes', 'y'}
    no_choice = {'no', 'n'}
    try:
        value = None
        while value != 1:
            with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
                value = f.read().strip()
            if value == "1":
                print("[+] Port Forwarding enabled we can proceed.")
                value = 1
            elif value == "0":
                confirmation = str(input("Port Forwarding should be enabled? y/n ").lower().strip())
                if confirmation in yes_choice:
                    subprocess.call(
                        "echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward",
                        shell=True,
                        stdout=DEVNULL,
                        )
                    value = subprocess.call(
                        "cat /proc/sys/net/ipv4/ip_forward",
                        shell=True,
                        stdout=DEVNULL,
                    )
                # elif confirmation.startswith("n"): also an option
                elif confirmation in no_choice:
                    print("[-] Operation cancelled. Have a nice day! ")
                    exit()
    except ValueError as e:
        print("[-] Unexpected value " + str(e))
    except OSError:
        print(
            "The file /proc/sys/net/ipv4/ip_forward was not found. System may not support IP forwarding or is not Linux.")
    except Exception as e:
        print("An error occurred while trying to connect. " + str(e))


