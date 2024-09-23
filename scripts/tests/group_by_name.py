from connect import connect_to_db


# Joins the two tables into one by municipality and period
# Then groups by period
query = """
SELECT municipality_water_power.municipality_name, 
    SUM(municipality_water_power.water_prod) AS water_prod, 
    SUM(municipality_solar_power.solar_prod) AS solar_prod, 
    municipality_water_power.period_year
FROM municipality_water_power
FULL OUTER JOIN municipality_solar_power
ON municipality_water_power.municipality_name = municipality_solar_power.municipality_name
AND municipality_water_power.period_year = municipality_solar_power.period_year
GROUP BY municipality_water_power.municipality_name, municipality_water_power.period_year
ORDER BY municipality_water_power.period_year
"""


def group_by_name():
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    return result
