from scapy.all import Ether, IP, UDP, Raw, wrpcap

packets = []

# Create 3 Modbus RTU request/response exchanges
for i in range(1, 4):
    # Request: Read Holding Registers from Slave 1
    req = Ether(src="00:11:22:33:44:55", dst="66:77:88:99:AA:BB") / \
          IP(src="192.168.1.100", dst="192.168.1.10") / \
          UDP(sport=1502, dport=502) / \
          Raw(load=bytes.fromhex("01 03 00 00 00 02 C4 0B"))

    # Response: Slave 1 returns 2 registers (4 bytes of data)
    resp = Ether(src="66:77:88:99:AA:BB", dst="00:11:22:33:44:55") / \
           IP(src="192.168.1.10", dst="192.168.1.100") / \
           UDP(sport=502, dport=1502) / \
           Raw(load=bytes.fromhex("01 03 04 00 0A 00 14 F0 1C"))

    packets.extend([req, resp])

wrpcap("modbus_rtu_only.pcap", packets)
print("Created modbus_rtu_only.pcap with bidirectional traffic")
