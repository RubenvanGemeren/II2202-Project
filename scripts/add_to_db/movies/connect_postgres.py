import psycopg2


def get_connection(host, port, database, user, password):
    try:
        conn = psycopg2.connect(
            host=host, port=port, database=database, user=user, password=password
        )
        conn.autocommit = True
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        exit()
