from scapy.all import Ether, IP, UDP, Raw, wrpcap

# Modbus RTU payload: Read Holding Registers
payload = bytes.fromhex("01 03 00 00 00 02 C4 0B")  # Slave 1, Function 3, CRC

# Create packet
pkt = Ether(src="00:11:22:33:44:55", dst="66:77:88:99:AA:BB") / \
      IP(src="192.168.1.100", dst="192.168.1.10") / \
      UDP(sport=1502, dport=502) / \
      Raw(load=payload)

# Write to PCAP
wrpcap("modbus_rtu_only.pcap", [pkt])
print("✅ Created modbus_rtu_only.pcap")
