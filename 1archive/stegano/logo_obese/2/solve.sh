#!bash
dd if=./stage2.png of=stage3.png bs=12 count=1
dd if=./stage2.png of=stage3.png oflag=append conv=notrunc bs=45 skip=1
