#!bash

filename="flag_c0rr_pt3d.png"
cp ../1/"$filename" ./
# printf '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a' | dd of=$filename bs=1 seek=0 conv=notrunc
printf '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00' | dd of=$filename bs=1 seek=0 conv=notrunc #fix signature and header

printf '\x6c\x55\xbb\xd4' | dd of=$filename bs=1 seek=29 conv=notrunc # fix ihdr crc

# file fixed enough to open with gimp
