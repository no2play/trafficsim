from scapy.all import *
import time

# 1. กำหนดชื่อไฟล์ผลลัพธ์
filename = "loop_test_storm.pcap"
packets = []

print("Generating packets...")

# 2. สร้าง ARP Request จำนวนมาก (จำลอง Storm)
# เปลี่ยน hwsrc เป็น MAC ของ Switch หรืออุปกรณ์ต้นทางที่สมมติว่าเกิด Loop
for i in range(1000): 
    pkt = Ether(src="00:1c:0e:87:85:04", dst="ff:ff:ff:ff:ff:ff") / \
          ARP(pdst=f"192.168.1.{i%254}", hwdst="ff:ff:ff:ff:ff:ff")
    packets.append(pkt)

# 3. บันทึกเป็นไฟล์ PCAP
wrpcap(filename, packets)

print(f"Successfully created {filename} with {len(packets)} packets!")
