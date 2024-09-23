import pandas as pd


benchmark_v7_path = "../data/similar_data/GPU_benchmarks_v7.csv"
benchmark_scores_api_path = "../data/similar_data/GPU_scores_graphicsAPIs.csv"


def load():

    benchmark_v7_df = pd.read_csv(benchmark_v7_path)
    benchmark_scores_api_df = pd.read_csv(benchmark_scores_api_path)

    return benchmark_v7_df, benchmark_scores_api_df
