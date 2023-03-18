#!bash
names=$(tshark -nr ./capture-reseau.pcapng -Y 'dns.qry.name matches "hallebarde" and ip.src == 192.168.122.55' | cut -d" " -f12 | cut -d"." -f1)

for i in $names
do
	rax2 -s <<<$i
done

flagfilenames="404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}" # used : | strings  | grep begin | awk -F "begin" '{print $1}'

