#!/bin/bash

function compress_and_split {
    echo "Compressing ${1}"
    zip -r ${1}/metrics-q-network.zip ${1}/metrics-q-network -x *-MBP.home -x .DS_Store -s 64
}  

compress_and_split 201609040550_5010eps
compress_and_split 201609111241_2700eps
compress_and_split 201609111241_7300eps
compress_and_split 201609160922_54eps
compress_and_split 201609171218_175eps


