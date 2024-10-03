import numpy as np
import random
from queries import (
    get_id_array,
    select_by_id,
    select_by_range,
    join_game_lineups_and_players,
    group_by_season,
    select_by_name,
)

from connect_postgres import connect_to_db

from write import write_benchmark_to_file


def ratings_by_id():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    ids = get_id_array(cursor=cursor)

    for item in range(1000):
        print(item)
        execution_time, _ = select_by_id(cursor=cursor, id=random.choice(ids))
        benchmarks = np.append(benchmarks, execution_time)
    write_benchmark_to_file("benchmarks/gin_index/game_lineups_by_id.txt", benchmarks)


def ratings_by_range():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for item in range(1000):
        print(item)
        execution_time, _ = select_by_range(cursor=cursor, date_min="2013-07-27", date_max="2016-01-01")
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/gin_index/game_lineups_by_range.txt", benchmarks)


def join_game_lineups_players():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for item in range(1000):
        print(item)
        execution_time, _ = join_game_lineups_and_players(
            cursor=cursor
        )
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/gin_index/join_game_lineups_players.txt", benchmarks)


def join_and_group_by_season():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for item in range(1000):
        print(item)
        execution_time, _ = group_by_season(cursor=cursor)
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/gin_index/group_by_season.txt", benchmarks)


def players_by_names():
    conn = connect_to_db()
    cursor = conn.cursor()

    benchmarks = np.array([])

    for item in range(1000):
        print(item)
        execution_time, _ = select_by_name(cursor=cursor, name="Marc")
        benchmarks = np.append(benchmarks, execution_time)

    write_benchmark_to_file("benchmarks/gin_index/players_by_names.txt", benchmarks)


ratings_by_id()
ratings_by_range()
join_game_lineups_players()
join_and_group_by_season()
players_by_names()
