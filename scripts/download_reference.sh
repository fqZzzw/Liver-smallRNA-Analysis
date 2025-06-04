#!/bin/bash
set -e

# 创建目录
mkdir -p data/index data/gtf

echo "正在下载 GRCh38 基因组 FASTA..."
wget -c https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_44/GRCh38.primary_assembly.genome.fa.gz -O data/index/GRCh38.primary_assembly.genome.fa.gz

echo "解压 FASTA..."
gunzip -c data/index/GRCh38.primary_assembly.genome.fa.gz > data/index/GRCh38.primary_assembly.genome.fa

echo "正在下载 GTF 注释文件..."
wget -c https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_44/gencode.v44.annotation.gtf.gz -O data/gtf/Homo_sapiens.GRCh38.gtf.gz

echo "解压 GTF..."
gunzip -c data/gtf/Homo_sapiens.GRCh38.gtf.gz > data/gtf/Homo_sapiens.GRCh38.gtf

echo "参考基因组和注释文件下载完成！"
