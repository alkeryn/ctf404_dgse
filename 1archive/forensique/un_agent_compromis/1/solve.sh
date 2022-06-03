#!bash
tshark -nr ./capture-reseau.pcapng --export-objects http,tmp
mv tmp/exfiltration.py ./
rm -rf tmp
