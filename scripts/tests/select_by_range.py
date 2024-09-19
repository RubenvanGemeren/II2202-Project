from connect import connect_to_db

# Ranged query
query = """
SELECT *
FROM municipality_water_power
WHERE municipality_name = %s AND water_prod BETWEEN %s AND %s
"""


def select_by_range(name: str, lower: str, upper: str):
    con = connect_to_db()
    cursor = con.cursor()

    try:
        print(name)

        cursor.execute(
            query,
            (name, lower, upper),
        )

        result = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        result = e

    return result
