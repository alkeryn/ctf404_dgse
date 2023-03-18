#!bash
# names=$(tshark -nr ./capture-reseau.pcapng -Y 'dns.qry.name matches "hallebarde" and ip.src == 192.168.122.55' | cut -d" " -f12 | cut -d"." -f1)
names=$(tshark -nr ./capture-reseau.pcapng -Y 'dns.qry.name matches "hallebarde" and ip.src == 192.168.122.1' | cut -d" " -f13 | cut -d"." -f1)

for i in $names
do
	echo $i
done

flagfilenames="404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}" # used : | strings  | grep begin | awk -F "begin" '{print $1}'

40CTF{DNS_3xf1ltrnhaebd}
404CTF{DNS_3xf1ltrat1on_hallebarde}
