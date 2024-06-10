#!/bin/bash

for file in $(find . -name "*.bed")
do
name=${file%%.bed*}
$(awk '{print $1,$2,$3,$7,".",$9,$5,$6,"255,0,0","3","1,"$6-$5",1","0,"$5-$2","$3-$2-1, $8}' $file | sed s/' '/'\t'/g > ${name}".gappedPeak")
done
