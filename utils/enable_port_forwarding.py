#/usr/bin/env python
import subprocess

def enable_port_fowarding():
    confirmation = input("Do you wish to enable port forwarding? (Y/n): ").lower().strip()
    if confirmation.startswith("y"):
        print("[+] Processing...")
        subprocess.call(["echo", 1, "|", "sudo", "tee", "/proc/sys/net/ipv4/ip_forward"])
        print("[+] Checking if Port Forwarding is enabled")
    else:
        print("[-] Operation cancelled. Have a nice day! ")
        exit()

def check_port_forwarding():
    try:
        with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
            value = f.read().strip()
        if value == "1":
            print("[+] Port Forwarding enabled we can proceed.")
        elif value == "0":
            print("[-] Port Forwarding disabled. Let's enable.")
            subprocess.call("echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward", shell=True)
            exit()
        else:
            print("[-] Unexpected value " + str(value))
            exit()
    except OSError:
        print(
            "The file /proc/sys/net/ipv4/ip_forward was not found. System may not support IP forwarding or is not Linux.")
    except Exception as e:
        print("An error occurred while trying to connect. " + str(e))

def disable_port_forwarding():
	print("[+] Ctrl C Exiting: Disabling port forwarding. ")
	subprocess.call("echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward", shell=True)
	with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
		value = f.read().strip()
		if value == "0":
			print("[+] Port Forwarding disabled. Bye bye keep smiling.")
			exit()
		else:
			print("[+] Something went wrong.  Manually disable.")
			exit()