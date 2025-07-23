from scapy.all import *

# IEC 60870-5-101 fixed frame (example): 10 49 00 49
# Simulated request and response
req_frame = bytes.fromhex("10 49 00 49")
resp_frame = bytes.fromhex("10 E9 00 E9")

pkts = []

for i in range(5):
    # Simulate request from client to server
    req = Ether()/IP(src="192.168.1.10", dst="192.168.1.20")/UDP(sport=2405, dport=2404)/Raw(load=req_frame)
    # Simulate response from server to client
    resp = Ether()/IP(src="192.168.1.20", dst="192.168.1.10")/UDP(sport=2404, dport=2405)/Raw(load=resp_frame)
    pkts.extend([req, resp])

wrpcap("iec101_simulated.pcap", pkts)
