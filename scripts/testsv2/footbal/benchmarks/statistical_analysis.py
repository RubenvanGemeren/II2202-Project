import numpy as np
import numpy as np

index_types = [
    "no_index",
    "hash_index",
    "b_tree_index",
    "gin_index",
    "brin_index",
]

query_types = [
    "ratings_by_id",
    "ratings_by_range",
    "join_movies_ratings",
    "group_by_title",
    "movies_by_genres",
]


def read_benchmark_from_file(file_path: str) -> np.array:
    return np.loadtxt(file_path)


def write_benchmarks_to_file(file_path: str, benchmarks: list):
    with open(file_path, "w") as f:
        for item in benchmarks:
            f.write("%s\n" % item)


values = np.array([])

for index in index_types:
    for query in query_types:
        file_path = f"benchmarks/{index}/{query}.txt"
        benchmarks = read_benchmark_from_file(file_path)
        values = np.append(values, f"{index} {query}: ")
        values = np.append(values, "mean: " + str(benchmarks.mean()) + ",")
        values = np.append(
            values, "median: " + str(benchmarks[len(benchmarks) // 2]) + ","
        )
        values = np.append(values, "std. dev: " + str(benchmarks.std()) + ",")
        values = np.append(values, "variance: " + str(benchmarks.var()) + ",")
        values = np.append(values, "\n")

write_benchmarks_to_file("benchmarks/statistical_analysis.txt", values)
