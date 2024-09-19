import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="credentials.env")

postgres_url = "postgresql://II2202-project-storage_owner:2nAJECiQ7zYL@ep-withered-block-a2wwcz46.eu-central-1.aws.neon.tech/II2202-project-storage?sslmode=require&options=endpoint%3Dep-withered-block-a2wwcz46"

database = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def connect_to_db():
    try:
        # conn = psycopg2.connect(postgres_url)
        conn = psycopg2.connect(database=database, user=db_user, password=db_password)
        conn.autocommit = True
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        exit()
