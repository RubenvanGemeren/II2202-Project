from connect import connect_to_db


query = """
SELECT * 
FROM municipality_water_power
WHERE municipality_name = %s
"""


def select_by_name(name: str):
    con = connect_to_db()
    cursor = con.cursor()

    print(name)

    cursor.execute(
        query,
        (name,),
    )

    result = cursor.fetchall()

    return result
