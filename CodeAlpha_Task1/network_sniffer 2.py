from scapy.all import *
from datetime import datetime

packet_count = 0

def packet_info(packet):
    global packet_count
    packet_count += 1

    print("=" * 60)
    print("Packet Number :", packet_count)
    print("Time          :", datetime.now().strftime("%H:%M:%S"))

    if packet.haslayer(IP):
        print("Source IP     :", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol      :", packet[IP].proto)

    if packet.haslayer(Raw):
        print("Payload       :", packet[Raw].load)

sniff(prn=packet_info, count=10)
