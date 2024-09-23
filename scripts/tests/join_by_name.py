from connect import connect_to_db


# Joins the two tables into one by municipality and period
query = """
SELECT * 
FROM municipality_water_power
FULL OUTER JOIN municipality_solar_power
ON municipality_water_power.municipality_name = municipality_solar_power.municipality_name
AND municipality_water_power.period_year = municipality_solar_power.period_year
"""


def join_by_name():
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    return result
