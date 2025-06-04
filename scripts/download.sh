#!/bin/bash
mkdir -p data/raw && cd data/raw

for srr in SRR8713489 SRR8713490 SRR8713491 SRR8713492 SRR8713493 SRR8713494
do
    prefetch $srr
    fasterq-dump $srr --gzip
    echo "$srr 下载完成"
done
