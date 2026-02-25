from scapy.all import *

# สร้าง STP Configuration BPDU (Topology Change) แบบดิบ
# \x00\x00\x00\x01 = Proto ID 0, Version 0, BPDU Type 0, Flags 0x01 (TC)
stp_raw_payload = b"\x00\x00\x00\x01\x80\x00\x00\x1c\x0e\x87\x78\x00\x00\x00\x00\x04\x80\x04\x00\x00"

filename = "final_loop_test.pcap"
packets = []

print("Generating 10,000 High-Intensity Loop Packets...")
for i in range(10000):
    # ใช้ LLC Layer หุ้ม STP Payload
    pkt = Dot3(dst="01:80:c2:00:00:00", src="00:1c:0e:87:85:04") / \
          LLC(dsap=0x42, ssap=0x42, ctrl=3) / \
          Raw(load=stp_raw_payload)
    packets.append(pkt)

wrpcap(filename, packets)
print(f"Done! PCAP generated: {filename}")
