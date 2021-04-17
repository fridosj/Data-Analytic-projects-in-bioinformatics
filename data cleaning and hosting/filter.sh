#!/bin/sh
num=1
for f in *.csv
do
	name="CHR${num}"
	awk -F, 'length($11) > 10 { print($11) }' $f > $name.txt
	num=$(expr $num + 1)
done