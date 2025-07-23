from scapy.all import Ether, IP, UDP, Raw, wrpcap

packets = []

# Create 3 IEC101 exchanges (simplified)
for i in range(1, 4):
    # Request: Fixed-length frame (start=0x10)
    req = Ether(src="00:11:22:33:44:56", dst="66:77:88:99:AA:BC") / \
          IP(src="192.168.1.101", dst="192.168.1.20") / \
          UDP(sport=2405, dport=2404) / \
          Raw(load=bytes.fromhex("10 49 00 49"))

    # Response: Acknowledgement or control command (example)
    resp = Ether(src="66:77:88:99:AA:BC", dst="00:11:22:33:44:56") / \
           IP(src="192.168.1.20", dst="192.168.1.101") / \
           UDP(sport=2404, dport=2405) / \
           Raw(load=bytes.fromhex("10 0B 00 0B"))

    packets.extend([req, resp])

wrpcap("iec101_only.pcap", packets)
print("Created iec101_only.pcap with bidirectional traffic")
