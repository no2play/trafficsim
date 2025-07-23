from scapy.all import Ether, IP, UDP, Raw, wrpcap

# IEC 60870-5-101 example payload (fixed frame)
payload = bytes.fromhex("10 49 00 49")

# Create packet
pkt = Ether(src="00:11:22:33:44:56", dst="66:77:88:99:AA:BC") / \
      IP(src="192.168.1.101", dst="192.168.1.20") / \
      UDP(sport=2405, dport=2404) / \
      Raw(load=payload)

# Write to PCAP
wrpcap("iec101_only.pcap", [pkt])
print("✅ Created iec101_only.pcap")
