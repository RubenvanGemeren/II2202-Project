import psycopg2


postgres_url = "postgresql://II2202-project-storage_owner:2nAJECiQ7zYL@ep-withered-block-a2wwcz46.eu-central-1.aws.neon.tech/II2202-project-storage?sslmode=require&options=endpoint%3Dep-withered-block-a2wwcz46"


def connect_to_db():
    try:
        conn = psycopg2.connect(postgres_url)
        conn.autocommit = True
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        exit()
