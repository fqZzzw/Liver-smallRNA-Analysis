#!/bin/bash
cd data/index
hisat2-build GRCh38.primary_assembly.genome.fa grch38_index
cd ../../

cd data/clean
mkdir -p ../bam

for fq in *.clean.fq.gz
do
    base=$(basename $fq .clean.fq.gz)
    hisat2 -x ../index/grch38_index \
        -U $fq \
        -S ../bam/${base}.sam

    samtools view -bS ../bam/${base}.sam | samtools sort -o ../bam/${base}.sorted.bam
    samtools index ../bam/${base}.sorted.bam
    rm ../bam/${base}.sam
done
