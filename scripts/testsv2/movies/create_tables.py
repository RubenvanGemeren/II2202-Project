import psycopg2

create_movies_table = """
CREATE TABLE movies(
    movieId INTEGER PRIMARY KEY,
    title VARCHAR,
    budget INTEGER,
    genres VARCHAR[]
);
"""

create_ratings_table = """
CREATE TABLE ratings(
    id SERIAL PRIMARY KEY,
    userId INTEGER,
    movieId INTEGER REFERENCES movies(movieId),
    rating REAL
);
"""


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="postgres",
            user="user",
            password="secret",
        )
        conn.autocommit = True
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")


conn = connect_to_db()
cursor = conn.cursor()

cursor.execute(create_movies_table)
cursor.execute(create_ratings_table)
