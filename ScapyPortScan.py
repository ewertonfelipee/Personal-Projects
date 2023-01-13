import sys
from scapy.all import *

if len(sys.argv) < 2:
	print("Scapy Port Scan by EWERTON FELIPE")
	print("Usage: python3 script.py target")
	
else:
	ports = input("Enter with the ports (Space-Separated): ")
	portas = ports.split() # string to list
	int_ports = list(map(int, portas)) # convert list of string in list of int
	conf.verb = 0 # without verbose
	
	pIP = IP(dst=sys.argv[1])
	pTCP = TCP(dport=int_ports, flags="S")
	packet = pIP/pTCP
	resp, nonresp = sr(packet)
	for response in resp:
		sPorts = response[1][TCP].sport
		flag = response[1][TCP].flags
		if(flag == "SA"):
			print(f"Opened Port: {sPorts}")
