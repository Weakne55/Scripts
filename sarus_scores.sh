#!/bin/bash

file=$1
name="24hpf"
mkdir $name"/sarus_output" $name"/pwm_logpvalue" $name"/gappedPeak"
for pwm in $(ls pwms)
do
var=($(ls "pwms/"$pwm))
#echo ${var[0]} ${var[1]}
$(java -jar ~/actual/sarus-2.1.0.jar ${file} "pwms/"$pwm$"/"${var[0]} besthit --pvalues-file "pwms/"$pwm"/"${var[1]} --output-scoring-mode logpvalue --output-bed > $name"."$pwm".bed")
$(cat $name"."$pwm".bed" | awk '{split($4, a, ";"); split(a[2], b, ":"); split(b[2], c, "-"); print $1, c[1], c[2], b[4], $2, $3, a[1], $5, $6}' | sed s/" "/'\t'/g > $name"."$pwm".logpvalue.bed")
$(awk '{print $1,$2,$3,$7,".",$9,$5,$6,"255,0,0","3","1,"$6-$5",1","0,"$5-$2","$3-$2-1, $8}' $name"."$pwm".logpvalue.bed" | sed s/' '/'\t'/g > $name"."$pwm".logpvalue.gappedPeak")
$(cat $name"."$pwm".logpvalue.gappedPeak" >> $name".TFBS.logpvalue.gappedPeak")
mv $name"."$pwm".bed" $name"/sarus_output"  
mv $name"."$pwm".logpvalue.bed" $name"/pwm_logpvalue" 
mv $name"."$pwm".logpvalue.gappedPeak" $name"/gappedPeak"
done

mv $name".TFBS.logpvalue.gappedPeak" $name"/"
