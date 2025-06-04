#!/bin/bash
mkdir -p data/clean && cd data/raw

for fq in *.fastq.gz
do
    base=$(basename $fq .fastq.gz)
    fastp -i $fq \
          -o ../clean/${base}.clean.fq.gz\
          -h ../clean/${base}.html -j ../clean/${base}.json
done

cd ../clean
fastqc *.clean.fq.gz
multiqc .
