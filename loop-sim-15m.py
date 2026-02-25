from scapy.all import *
import time

# สร้าง STP Configuration BPDU (Topology Change) แบบ Raw
stp_raw_payload = b"\x00\x00\x00\x01\x80\x00\x00\x1c\x0e\x87\x78\x00\x00\x00\x00\x04\x80\x04\x00\x00"
filename = "loop_15mins_test.pcap"
packets = []

duration_min = 15
packets_per_second = 100 # ส่ง 100 packets ทุกวินาที เพื่อสร้างปริมาณที่สม่ำเสมอ

print(f"Generating Loop traffic for {duration_min} minutes...")

total_seconds = duration_min * 60
start_time = time.time()

for s in range(total_seconds):
    for i in range(packets_per_second):
        # สร้าง Packet พร้อมใส่ Timestamp ปัจจุบันลงไปเพื่อให้ Nozomi อ่านค่าเวลาได้ต่อเนื่อง
        pkt = Dot3(dst="01:80:c2:00:00:00", src="00:1c:0e:87:85:04") / \
              LLC(dsap=0x42, ssap=0x42, ctrl=3) / \
              Raw(load=stp_raw_payload)
        packets.append(pkt)
    
    # แสดงความคืบหน้าทุก 1 นาที
    if (s + 1) % 60 == 0:
        print(f"Progress: {(s + 1) // 60} / {duration_min} minutes done.")

# บันทึกไฟล์
wrpcap(filename, packets)
print(f"Finished! File saved as {filename}")
