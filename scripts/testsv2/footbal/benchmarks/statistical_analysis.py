import numpy as np
import os

index_types = [
    "no_index",
    "hash_index",
    "b_tree_index",
    "gin_index",
    "brin_index",
]

query_types = [
    "game_lineups_by_id",
    "game_lineups_by_range",
    "group_by_season",
    "join_game_lineups_players",
    "players_by_names",
]


def read_benchmark_from_file(file_path: str) -> np.array:
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    return np.loadtxt(os.path.join(current_dir, file_path))


def write_benchmarks_to_file(file_path: str, benchmarks: list):
    # Ensure the directory exists
    # os.makedirs(os.path.dirname(file_path), exist_ok=True)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(current_dir, file_path), "w") as f:
        for item in benchmarks:
            f.write("%s\n" % item)


values = np.array([])

for index in index_types:
    for query in query_types:
        file_path = f"{index}/{query}.txt"
        benchmarks = read_benchmark_from_file(file_path)
        values = np.append(values, f"{index} {query}: ")
        values = np.append(values, "mean: " + str(benchmarks.mean()) + ",")
        values = np.append(
            values, "median: " + str(benchmarks[len(benchmarks) // 2]) + ","
        )
        values = np.append(values, "std. dev: " + str(benchmarks.std()) + ",")
        values = np.append(values, "variance: " + str(benchmarks.var()) + ",")
        values = np.append(values, "\n")

write_benchmarks_to_file("statistical_analysis.txt", values)
