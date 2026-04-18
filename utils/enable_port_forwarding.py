
import subprocess

subprocess.call(["echo", 1, "|", "sudo", "tee", "/proc/sys/net/ipv4/ip_forward"])