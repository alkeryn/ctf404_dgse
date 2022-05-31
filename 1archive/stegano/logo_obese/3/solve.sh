#!bash
zsteg -E imagedata ./stage3.png > out2
dd if=out2 of=stage4.png bs=946473 skip=1
rm out2
