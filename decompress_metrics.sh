#!/bin/bash

function merge_and_decompress {
    echo "Decompressing ${1}"
    mkdir ${1}/metrics-q-network 
    zip -FF ${1}/metrics-q-network.zip --out ${1}/temp.zip
    unzip ${1}/temp.zip
    rm ${1}/temp.zip
}  

merge_and_decompress 201609040550_5010eps
merge_and_decompress 201609111241_2700eps
merge_and_decompress 201609111241_7300eps
merge_and_decompress 201609160922_54eps
merge_and_decompress 201609171218_175eps


