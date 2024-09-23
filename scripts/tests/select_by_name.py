from connect import connect_to_db

# Selects all by municipality
query = """
SELECT * 
FROM municipality_water_power
WHERE municipality_name = %s
"""


def select_by_name(name: str):
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(
        query,
        (name,),
    )

    result = cursor.fetchall()

    return result
