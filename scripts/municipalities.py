import requests

municipalities_endpoint = "http://api.kolada.se/v2/municipality?title="


response = requests.get(municipalities_endpoint)
municipalities = response.json()["values"]

def fetch_municipalities():
    municipalities_array = []
    for municipality in municipalities:
        municipality_name = municipality["title"]
        municipality_id = municipality["id"]

        municipalities_array.append({
            "name": municipality_name,
            "id": municipality_id
        })

    return municipalities_array


