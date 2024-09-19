from dotenv import load_dotenv
import os
from power_data import fetch_power_data
import psycopg2

load_dotenv(dotenv_path="credentials.env")

# Check if this works
if os.getenv("ENV") == "":
    print("No environment found or incomplete")
    exit()

postgres_url = "postgresql://II2202-project-storage_owner:2nAJECiQ7zYL@ep-withered-block-a2wwcz46.eu-central-1.aws.neon.tech/II2202-project-storage?sslmode=require&options=endpoint%3Dep-withered-block-a2wwcz46"

# Get database name from environment variable
database = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

print(database)

# Queries
create_water_table_query = """ CREATE TABLE IF NOT EXISTS municipality_water_power(id SERIAL PRIMARY KEY, municipality_name TEXT NOT NULL, municipality_id INTEGER, power_type TEXT, period_year INTEGER,water_prod double precision); """

create_solar_table_query = """ CREATE TABLE IF NOT EXISTS municipality_solar_power(id SERIAL PRIMARY KEY, municipality_name TEXT NOT NULL, municipality_id INTEGER, power_type TEXT, period_year INTEGER, solar_prod double precision); """

insert_water_query = """
INSERT INTO municipality_water_power (municipality_name, municipality_id, power_type, period_year, water_prod)
VALUES (%s, %s, %s, %s, %s)
"""

insert_solar_query = """
INSERT INTO municipality_solar_power (municipality_name, municipality_id, power_type, period_year, solar_prod)
VALUES (%s, %s, %s, %s, %s)
"""

def connect_to_db():
    try:
        conn = psycopg2.connect(database=database, user=db_user, password=db_password)
        conn.autocommit = True
        cursor = conn.cursor()
        print("Connection successful!")
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        exit()

    return cursor

def create_tables():
    cursor = connect_to_db()

    # Check if tables exist, if not create them
    cursor.execute(create_water_table_query)
    cursor.execute(create_solar_table_query)

    cursor.close()



def create_model():
    create_tables()

    cursor = connect_to_db()

    water_data, solar_data = fetch_power_data()

    for data in water_data:
        cursor.execute(
            insert_water_query,
            (
                data["name"],
                data["id"],
                data["power_type"],
                data["period_year"],
                data["water_prod"],
            ),
        )

    for data in solar_data:
        cursor.execute(
            insert_solar_query,
            (
                data["name"],
                data["id"],
                data["power_type"],
                data["period_year"],
                data["solar_prod"],
            ),
        )