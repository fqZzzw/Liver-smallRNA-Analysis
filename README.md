# Liver-smallRNA-Seq-Differential-Analysis

https://opensource.org/licenses/MIT

https://www.python.org/

https://docs.conda.io/

本项目对肝癌细胞(Huh7)、丙型肝炎患者肝细胞(HCV)和正常肝细胞(NL)进行small RNA-seq差异表达分析，旨在探索三种肝细胞的小RNA表达差异，识别潜在的疾病治疗靶点。

## 项目摘要

利用GEO数据库中GSE128164项目的公开数据，通过搭建conda环境，使用生物信息学工具链对三种肝细胞类型的转录组数据进行比较分析：

1. ​**​数据获取​**​：从NCBI SRA下载6个small RNA测序样本
2. ​**​数据处理​**​：使用fastp进行质量控制，HISAT2进行序列比对
3. ​**​基因定量​**​：使用featureCounts生成表达矩阵
4. ​**​差异分析​**​：Python实现的Welch's t-test和FDR校正
5. ​**​可视化​**​：生成火山图和热图展示差异表达基因

 **​关键发现​**​：

- HCV感染特异性扰乱部分非编码RNA表达
- 肝癌细胞存在全局性小RNA表达紊乱
- HCV感染组与肝癌组的基因表达谱高度相似

## 目录结构

```
├── data/                   # 数据目录（需手动下载）
│   ├── raw/                # 原始测序数据
│   ├── clean/              # 清洗后数据
│   ├── index/              # 参考基因组索引
│   └── gtf/                # 注释文件
├── scripts/                # 分析脚本
│   ├── download_reference.sh   # 下载参考基因组
│   ├── download.sh         # 下载SRA数据
│   ├── qc_trim.sh          # 质控与清洗
│   ├── mapping.sh          # 序列比对
│   ├── featurecounts.sh    # 表达量计数
│   └── analysis.py         # 差异分析与可视化
├── results/                # 分析结果
│   ├── volcano_*.png       # 火山图
│   ├── heatmap_*.png       # 热图
│   └── diffexpr_*.csv      # 差异表达基因
├── report/                 # 项目报告
│   └── report.md           # Markdown格式报告
├── env.yml                 # Conda环境配置
└── README.md               # 项目说明
```

## 安装与使用

### 1. 克隆仓库

```
git clone https://github.com/your_username/Liver-smallRNA-Analysis.git
cd Liver-smallRNA-Analysis
```

### 2. 创建Conda环境

```
conda env create -f env.yml
conda activate rnaseq_env
```

### 3. 下载参考基因组

```
bash scripts/download_reference.sh
```

### 4. 下载SRA数据

```
bash scripts/download.sh
```

### 5. 运行分析流程

```
# 数据质量控制与清洗
bash scripts/qc_trim.sh

# 序列比对
bash scripts/mapping.sh

# 表达量计数
bash scripts/featurecounts.sh

# 差异表达分析
python scripts/analysis.py
```

## 数据来源

- GEO项目: [GSE128164](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128164)
- 样本信息:

|样本编号|类型|描述|
|---|---|---|
|SRR8713489, SRR8713490|Huh7|肝癌细胞系|
|SRR8713491, SRR8713492|NL|正常肝细胞|
|SRR8713493, SRR8713494|HCV|HCV患者肝细胞|

## 许可证

本项目采用 MIT 许可证

## 参考文献

1. Goodgame, Boone et al. (2003). Am J Gastroenterol
2. Kim, Daehwan et al. (2015). Nat Methods
3. Liao, Yang et al. (2014). Bioinformatics
