from power_data import fetch_power_data
from urllib.parse import urlparse
import psycopg2

postgres_url = "postgresql://II2202-project-storage_owner:2nAJECiQ7zYL@ep-withered-block-a2wwcz46.eu-central-1.aws.neon.tech/II2202-project-storage?sslmode=require&options=endpoint%3Dep-withered-block-a2wwcz46"

insert_water_query = """
INSERT INTO municipality_water_power (municipality_name, municipality_id, power_type, period_year, water_prod)
VALUES (%s, %s, %s, %s, %s)
"""

insert_solar_query = """
INSERT INTO municipality_solar_power (municipality_name, municipality_id, power_type, period_year, solar_prod)
VALUES (%s, %s, %s, %s, %s)
"""

def create_model():
    try:
        
        conn = psycopg2.connect(postgres_url)
        conn.autocommit = True
        cursor = conn.cursor()
        print("Connection successful!")
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        exit()

    water_data, solar_data = fetch_power_data()

    for data in water_data:
        cursor.execute(insert_water_query, (data["name"], data["id"], data["power_type"], data["period_year"], data["water_prod"]))
    
    for data in solar_data:
        cursor.execute(insert_solar_query, (data["name"], data["id"], data["power_type"], data["period_year"], data["solar_prod"]))


    



