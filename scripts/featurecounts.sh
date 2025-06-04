#!/bin/bash
mkdir -p counts
cd data/bam
featureCounts -a ../gtf/Homo_sapiens.GRCh38.gtf \
              -o ../../counts/gene_counts.txt \
              -T 4 *.sorted.bam
