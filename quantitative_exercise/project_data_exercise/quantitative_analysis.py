from read_gpu_datasets import load
import numpy as np

import matplotlib.pyplot as plt


benchmark_v7_df, benchmark_scores_api_df = load()

print("benchmark_v7_df\n", benchmark_v7_df.head())
# print("benchmark_scores_api_df\n", benchmark_scores_api_df.head())

print("benchmark_v7_df\n", benchmark_v7_df.info())
# print("benchmark_scores_api_df\n", benchmark_scores_api_df.info())

print("benchmark_v7_df null values\n", benchmark_v7_df.isnull().sum())
# print("benchmark_scores_api_df null values\n", benchmark_scores_api_df.isnull().sum())


benchmark_v7_df.drop(
    columns=["gpuName", "category", "powerPerformance", "TDP"], inplace=True
)

v7_corr = benchmark_v7_df.corr()

plt.figure(figsize=(10, 10))
plt.matshow(v7_corr, fignum=1)
plt.xticks(range(len(v7_corr.columns)), v7_corr.columns, rotation=90)
plt.yticks(
    range(len(v7_corr.columns)),
    v7_corr.columns,
)

fig = plt.gcf()
fig.savefig("figures/correlation_matrix.png")


plt.clf()
plt.hist(benchmark_v7_df["price"])
plt.ylabel("Count")
plt.xlabel("Price")
plt.savefig("figures/price_distribution.png")


plt.clf()
plt.hist(benchmark_v7_df["G3Dmark"])
plt.ylabel("Count")
plt.xlabel("Score")
plt.savefig("figures/G3Dmark_distribution.png")

plt.clf()
plt.hist(benchmark_v7_df["G2Dmark"])
plt.ylabel("Count")
plt.xlabel("Score")
plt.savefig("figures/G2Dmark_distribution.png")


plt.clf()
plt.hist(benchmark_v7_df["gpuValue"])
plt.ylabel("Count")
plt.xlabel("Value")
plt.savefig("figures/gpuValue_distribution.png")

# Calculate mean
g3dmark_mean = np.mean(benchmark_v7_df["G3Dmark"])
g2dmark_mean = np.mean(benchmark_v7_df["G2Dmark"])

# Calculate median
g3dmark_median = np.median(benchmark_v7_df["G3Dmark"])
g2dmark_median = np.median(benchmark_v7_df["G2Dmark"])

# Calculate variance
g3dmark_variance = np.var(benchmark_v7_df["G3Dmark"])
g2dmark_variance = np.var(benchmark_v7_df["G2Dmark"])

# Calculate standard deviation
g3dmark_std = np.std(benchmark_v7_df["G3Dmark"])
g2dmark_std = np.std(benchmark_v7_df["G2Dmark"])

print("G3Dmark mean:", g3dmark_mean)
print("G2Dmark mean:", g2dmark_mean)

print("G3Dmark median:", g3dmark_median)
print("G2Dmark median:", g2dmark_median)

print("G3Dmark variance:", g3dmark_variance)
print("G2Dmark variance:", g2dmark_variance)

print("G3Dmark standard deviation:", g3dmark_std)
print("G2Dmark standard deviation:", g2dmark_std)
