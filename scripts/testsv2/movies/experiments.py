import numpy as np
import random
from queries import (
    get_id_array,
    select_by_id,
    select_by_range,
    join_movies_and_ratings,
    group_by_title,
    select_by_genres,
)

from connect_postgres import connect_to_db

from write import write_benchmark_to_file


def ratings_by_id():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    ids = get_id_array(cursor=cursor)

    for _ in range(1000):
        execution_time = select_by_id(cursor=cursor, id=random.choice(ids))
        benchmarks = np.append(benchmarks, execution_time)
    write_benchmark_to_file("benchmarks/brin_index/ratings_by_id.txt", benchmarks)


def ratings_by_range():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for _ in range(1000):
        execution_time = select_by_range(cursor=cursor, rating_min=2, rating_max=4)
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/brin_index/ratings_by_range.txt", benchmarks)


def join_movies_ratings():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for _ in range(1000):
        execution_time = join_movies_and_ratings(
            cursor=cursor,
        )
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/brin_index/join_movies_ratings.txt", benchmarks)


def join_and_group_by_title():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for _ in range(1000):
        execution_time = group_by_title(cursor=cursor)
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/brin_index/group_by_title.txt", benchmarks)


def movies_by_genres():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for _ in range(1000):
        execution_time = select_by_genres(cursor=cursor, genres=["Action", "Comedy"])
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/brin_index/movies_by_genres.txt", benchmarks)


ratings_by_id()
ratings_by_range()
join_movies_ratings()
join_and_group_by_title()
movies_by_genres()
