# Liver-smallRNA-Seq-Differential-Analysis

https://opensource.org/licenses/MIT  
https://www.python.org/
https://docs.conda.io/

This project performs differential expression analysis of small RNA-seq data from hepatocellular carcinoma cells (Huh7), hepatitis C virus (HCV)-infected liver cells, and normal liver cells (NL), aiming to explore the differences in small RNA expression among these three types of liver cells and identify potential therapeutic targets.

## 📝 Project Summary

Using publicly available data from GEO project GSE128164, we established a conda environment and employed a bioinformatics toolchain for comparative analysis of transcriptomic data from three liver cell types:

1. ​**​Data Acquisition​**​: Downloaded 6 small RNA-seq samples from NCBI SRA
2. ​**​Data Processing​**​: Quality control with fastp, sequence alignment with HISAT2
3. ​**​Gene Quantification​**​: Generated expression matrix using featureCounts
4. ​**​Differential Analysis​**​: Welch's t-test and FDR correction implemented in Python
5. ​**​Visualization​**​: Volcano plots and heatmaps for differentially expressed genes

🔑 ​**​Key Findings​**​:

- HCV infection specifically disrupts the expression of some non-coding RNAs
- Hepatocellular carcinoma cells show global dysregulation of small RNA expression
- HCV-infected cells and cancer cells exhibit highly similar gene expression profiles

## 📋 Directory Structure

```
├── data/                   # Data directory (manual download required)
│   ├── raw/                # Raw sequencing data
│   ├── clean/              # Cleaned data
│   ├── index/              # Reference genome index
│   └── gtf/                # Annotation files
├── scripts/                # Analysis scripts
│   ├── download_reference.sh   # Download reference genome
│   ├── download.sh         # Download SRA data
│   ├── qc_trim.sh          # Quality control and trimming
│   ├── mapping.sh          # Sequence alignment
│   ├── featurecounts.sh    # Expression quantification
│   └── analysis.py         # Differential analysis and visualization
├── results/                # Analysis results
│   ├── volcano_*.png       # Volcano plots
│   ├── heatmap_*.png       # Heatmaps
│   └── diffexpr_*.csv      # Differential expression results
├── report/                 # Project report
│   └── report.md           # Markdown format report
├── env.yml                 # Conda environment configuration
└── README.md               # Project description (English)
```

## ⚙️ Installation and Usage

### 1. Clone the repository

```
git clone https://github.com/your_username/Liver-smallRNA-Analysis.git
cd Liver-smallRNA-Analysis
```

### 2. Create Conda environment

```
conda env create -f env.yml
conda activate rnaseq_env
```

### 3. Download reference genome

```
bash scripts/download_reference.sh
```

### 4. Download SRA data

```
bash scripts/download.sh
```

### 5. Run the analysis pipeline

```
# Quality control and data cleaning
bash scripts/qc_trim.sh

# Sequence alignment
bash scripts/mapping.sh

# Expression quantification
bash scripts/featurecounts.sh

# Differential expression analysis
python scripts/analysis.py
```


## 🔍 Data Source

- GEO Project: [GSE128164](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128164)
- Sample Information:

|Sample IDs|Type|Description|
|---|---|---|
|SRR8713489, SRR8713490|Huh7|Hepatocellular carcinoma cell line|
|SRR8713491, SRR8713492|NL|Normal liver cells|
|SRR8713493, SRR8713494|HCV|HCV-infected liver cells|

## 📜 License

This project is licensed under the [MIT License](https://yuanbao.tencent.com/chat/naQivTmsDa/LICENSE)

## 📚 References

1. Goodgame, Boone et al. (2003). Am J Gastroenterol
2. Kim, Daehwan et al. (2015). Nat Methods
3. Liao, Yang et al. (2014). Bioinformatics
