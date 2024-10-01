import numpy as np
import os


def write_benchmark_to_file(path: str, arr: np.ndarray):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    current_dir = os.path.dirname(os.path.abspath(__file__))


    with open(os.path.join(current_dir, path), "w") as file:
        np.savetxt(file, arr)
