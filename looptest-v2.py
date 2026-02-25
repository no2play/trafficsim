from scapy.all import *
import random

filename = "network_loop_emergency.pcap"
packets = []

print("Generating Network Loop & Storm Scenario...")

# 1. จำลอง STP Topology Change (สัญญาณของการเสียบสายสลับไปมา)
for i in range(50):
    # สร้าง STP Config BPDU ที่บอกว่ามีการเปลี่ยนผัง (TC flag = 1)
    stp_pkt = Ether(dst="01:80:c2:00:00:00") / STP(type=0x00, proto=0, flags=0x01)
    packets.append(stp_pkt)

# 2. จำลอง ARP Storm (ผลกระทบจาก Loop)
# ส่ง 10,000 packets ด้วยความเร็วสูง (จำลองการวนลูปไม่รู้จบ)
for i in range(10000):
    # สุ่ม MAC ต้นทางจำลองว่า Loop ทำให้เกิดความสับสนในตาราง MAC Table
    rand_mac = "00:11:22:%02x:%02x:%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    arp_pkt = Ether(src=rand_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="192.168.1.254")
    packets.append(arp_pkt)

wrpcap(filename, packets)
print(f"Created {filename} successfully. Please import to Nozomi.")
