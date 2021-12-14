import argparse
import socket


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


parser = argparse.ArgumentParser(description='Port scanner')

parser.add_argument('ip', metavar='IP', type=str, help='IP address')

args = parser.parse_args()

ip = args.ip

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ip
port1 = 21
port2 = 22
port3 = 80
port4 = 110
port5 = 143
port6 = 443
port7 = 993
port8 = 995
print(f"[!] ***This may take  bit*** [!]")
print(f"\n[!] ****** TARGET: {ip} ****** [!] \n")


def portscanner(port):
    if sock.connect_ex((host, port)):
        print(bcolors.GREEN + "[*]Port %d is closed" % (port))
    else:
        print(bcolors.RED + "[!]Port %d is opened" % (port))


portscanner(port1)
portscanner(port2)
portscanner(port3)
portscanner(port4)
portscanner(port5)
portscanner(port6)
portscanner(port7)
portscanner(port8)
