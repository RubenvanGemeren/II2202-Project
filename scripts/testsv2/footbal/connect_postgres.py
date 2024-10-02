import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="credentials.env")

# Check if this works
if os.getenv("ENV") == "":
    print("No environment found or incomplete")
    exit()

# Get database name from environment variable
database = os.getenv("DB_NAME_FOOTBALL")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=database,
            user=db_user,
            password=db_password,
        )
        conn.autocommit = True
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
