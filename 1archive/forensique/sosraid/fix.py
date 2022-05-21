#!python3
disk0 = open("disk0.img","rb").read()
disk1 = open("disk1.img","rb").read()

disk2 = bytes(d0 ^ d1 for (d0, d1) in zip(disk0, disk1))

raidarray = [disk0, disk1, disk2]
BS = 1 # block size

#open our output disk file
with open('disk', 'wb') as f:
    #iterate over the blocks (disk length / 512 bytes per block)
    for blockIndex in range(len(disk0) // BS):
        #calculate our parity drive index rotating backwards, starting with the last drive
        parityIndex = (2 - blockIndex) % 3

        #iterate over the 3 drives in the array
        for driveIndex in range(3):
            #make sure not to pull data from the parity drive, we only want actual data
            if driveIndex != parityIndex:
                #calculate our starting byte position
                blockStart = blockIndex * BS

                #write the data from the starting byte to 512 bytes after it from the target drive
                f.write(raidarray[driveIndex][blockStart:blockStart + BS])
