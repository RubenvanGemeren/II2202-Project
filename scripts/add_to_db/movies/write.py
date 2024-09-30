import numpy as np


def write_benchmark_to_file(path: str, arr: np.ndarray):
    with open(path, "w") as file:
        np.savetxt(file, arr)
