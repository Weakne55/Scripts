#!/bin/bash

file=$1
for pwm in $(ls pwms)
do
var=($(ls "pwms/"$pwm))
#echo ${var[0]} ${var[1]}
$(java -jar ~/actual/sarus-2.1.0.jar ${file} "pwms/"$pwm$"/"${var[0]} besthit --pvalues-file "pwms/"$pwm"/"${var[1]} --output-scoring-mode logpvalue --output-bed > "24hpf."$pwm".bed")
$(cat "24hpf."$pwm".bed" | awk '{split($4, a, ";"); split(a[2], b, ":"); split(b[2], c, "-"); print $1, c[1], c[2], b[4], $2, $3, a[1], $5, $6}' | sed s/" "/'\t'/g > "24hpf."$pwm".logpvalue.bed")
done
