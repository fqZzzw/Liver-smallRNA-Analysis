import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("results", exist_ok=True)

#读取计数矩阵并过滤低表达基因
def read_count_matrix(file_path):
    df = pd.read_csv(file_path, sep="\t", comment="#", index_col=0)
    df = df.iloc[:, 5:]
    df.columns = ["tumor1", "tumor2", "normal1", "normal2", "hcv1", "hcv2"]
    df = df[(df > 10).any(axis=1)]
    return df

#差异分析
def diff_expr(group1, group2, name):

    noise = np.random.normal(0, 1e-6, group1.shape)
    group1_smooth = group1 + noise
    group2_smooth = group2 + noise

    logfc = np.log1p(group1_smooth.mean(axis=1)) - np.log1p(group2_smooth.mean(axis=1))

    pvals = [ttest_ind(group1_smooth.loc[gene], group2_smooth.loc[gene], equal_var=False)[1] for gene in group1.index]
    padj = multipletests(pvals, method='fdr_bh')[1]
    res = pd.DataFrame({"log2FC": logfc, "pval": pvals, "padj": padj}, index=group1.index)
    res.to_csv(f"results/{name}_diffexpr.csv")
    return res

#火山图函数
def volcano(res, name):
    res["sig"] = (res["padj"] < 0.05) & (res["log2FC"].abs() > 1)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=res, x="log2FC", y=-np.log10(res["padj"]), hue="sig",
                    palette={True: "red", False: "gray"}, edgecolor=None, alpha=0.7)
    plt.axhline(-np.log10(0.05), ls="--", c="black")
    plt.axvline(1, ls="--", c="blue")
    plt.axvline(-1, ls="--", c="blue")
    plt.title(f"Volcano Plot: {name.replace('_', ' ').title()}")
    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10 Adjusted P-value")
    plt.legend(title="Significant")
    plt.tight_layout()
    plt.savefig(f"results/volcano_{name}.png")
    plt.close()


#热图函数
def heatmap(df, res, name):

    sig_genes = res[(res["padj"] < 0.05) & (res["log2FC"].abs() > 1)].index

    if len(sig_genes) > 0:
        log_counts = np.log1p(df.loc[sig_genes])
        sns.clustermap(log_counts, cmap="RdBu_r", z_score=0, figsize=(10, 8))
        plt.savefig(f"results/heatmap_{name}.png")
        plt.close()
    else:
        print(f"No significant genes found for {name}")
        
#主函数
def main():
    df = read_count_matrix("counts/gene_counts.txt")
    
    tumor = df[["tumor1", "tumor2"]]
    normal = df[["normal1", "normal2"]]
    hcv = df[["hcv1", "hcv2"]]

    res1 = diff_expr(tumor, normal, "tumor_vs_normal")
    res2 = diff_expr(hcv, normal, "hcv_vs_normal")
    res3 = diff_expr(tumor, hcv, "tumor_vs_hcv")

    volcano(res1, "tumor_vs_normal")
    volcano(res2, "hcv_vs_normal")
    volcano(res3, "tumor_vs_hcv")

    heatmap(df, res1, "tumor_vs_normal")

if __name__ == "__main__":
    main()
