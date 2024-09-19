from connect import connect_to_db


query = """
SELECT * FROM municipality_water_power (municipality_name, municipality_id, power_type, period_year, water_prod)
VALUES (%s, %s, %s, %s, %s)
WHERE municipality_name = %s
"""


def select_by_name(name: str):
    con = connect_to_db()
    cursor = con.cursor()

    print(name)

    cursor.execute(
        query,
        (
            "name",
            "id",
            "power_type",
            "period_year",
            "water_prod",
            name,
        ),
    )


#    result = cursor.fetchall()

# return result
