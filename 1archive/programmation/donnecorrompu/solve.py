#!python
import base64
from bitstring import BitArray

b64 = { 'A':"000000", 'B':"000001", 'C':"000010", 'D':"000011", 'E':"000100", 'F':"000101", 'G':"000110", 'H':"000111", 'I':"001000", 'J':"001001", 'K':"001010", 'L':"001011",
        'M':"001100", 'N':"001101", 'O':"001110", 'P':"001111", 'Q':"010000", 'R':"010001", 'S':"010010", 'T':"010011", 'U':"010100", 'V':"010101", 'W':"010110", 'X':"010111",
        'Y':"011000", 'Z':"011001", 'a':"011010", 'b':"011011", 'c':"011100", 'd':"011101", 'e':"011110", 'f':"011111", 'g':"100000", 'h':"100001", 'i':"100010", 'j':"100011",
        'k':"100100", 'l':"100101", 'm':"100110", 'n':"100111", 'o':"101000", 'p':"101001", 'q':"101010", 'r':"101011", 's':"101100", 't':"101101", 'u':"101110", 'v':"101111",
        'w':"110000", 'x':"110001", 'y':"110010", 'z':"110011", '0':"110100", '1':"110101", '2':"110110", '3':"110111", '4':"111000", '5':"111001", '6':"111010", '7':"111011",
        '8':"111100", '9':"111101", '+':"111110", '/':"111111", '=':"",
}
shitmap = {
# unicode my ass
'А':"A",
'В':"B",
'К':"K",
'Н':"H",
'Т':"T",
'а':"a",
'е':"e",
'о':"o",
'р':"p",
'с':"c",
'у':"y",
'х':"x",
}

remove = {
",": "",
"@": "",
' ': "",
'!': "",
'#': "",
'#': "",
'$': "",
'%': "",
'&': "",
'(': "",
')': "",
'*': "",
'-': "",
':': "",
'<': "",
'>': "",
'?': "",
'[': "",
'\'': "",
'\n': "",
']': "",
'^': "",
'_': "",
'`': "",
'{': "",
'|': "",
'}': "",
'\\': "",
'"' : "",
'.' : "",
';' : "",
}

fucked = "Rmх%hZуА*6KQ"

def fixbase(base):
    fixedbase = ""
    for i in base:
        if i not in remove:
            if i in shitmap:
                fixedbase+=shitmap[i]
            else:
                fixedbase+=i

    fixedbase += '=' * (len(fixedbase)%4)
    print(fixedbase)
    return fixedbase

def basetocode(base):
    base = fixbase(base)
    # code = "" # useful to debug
    # for i in base:
    #     code+=b64[i]
    bytess = base64.b64decode(base)
    code = BitArray(bytess).bin
    return code.encode()

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('challenge.404ctf.fr', 30117))

file = b""

for i in range(250):
    m = sock.recv(4096).decode()
    print("message: "+m)
    bf = m.find("[")
    bf = m.find(":",bf)
    base = m[bf+2:]

    code = basetocode(base)
    file+=code

    sock.send(code+b"\n")

m = sock.recv(1024)
print(m.decode())

import struct
def tobin(binary):
    n = 8
    output = b""
    out = [binary[i:i+n] for i in range(0, len(binary), n)]

    for i in out:
        output+=struct.pack("B", int(i,2))
    return output

f = open("out.mp3", "wb")
f.write(tobin(file))
