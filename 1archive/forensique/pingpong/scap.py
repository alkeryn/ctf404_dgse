#!/bin/python
from scapy.all import rdpcap

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('./ping.pcapng')

a=True
# Let's iterate through every packet
for packet in packets:
    a = not a
    if(a):
        print(chr(packet.len - 28),end="")
