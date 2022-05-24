#!/bin/python
from scapy.all import *

flags = {
'C': 'CWR',
'E': 'ECE',
'U': 'URG',
'A': 'ACK',
'P': 'PSH',
'R': 'RST',
'S': 'SYN',
'F': 'FIN',
}


cumul = ""
hexcum =""

ignore=0
n=0
for packet in PcapReader("./ransomware1.pcapng"):
    if TCP in packet and packet["IP"].src == "172.17.0.1":
        b = ""
        tflag = packet['TCP'].flags
        for i in flags:
            if i & tflag:
                b+="1"
            else:
                b+="0"
        # o = hex(int(b,2))
        cumul+=b

import struct
def tobin(binary):
    n = 8
    output = b""
    out = [binary[i:i+n] for i in range(0, len(binary), n)]

    for i in out:
        output+=struct.pack("B", int(i,2))
    return output

f = open("./out.pdf", "wb")
f.write(tobin(cumul))
