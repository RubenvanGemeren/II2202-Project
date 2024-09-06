import requests
from municipalities import fetch_municipalities

data_endpoint = "http://api.kolada.se/v2/data/municipality/"

water_kpi = "N45927"
solar_kpi = "N45952"



def fetch_water_data(municipality_id):
    endpoint = f"{data_endpoint}{municipality_id}/kpi/{water_kpi}"

    response = requests.get(endpoint)
    data = response.json()

    return data

def fetch_solar_data(municipality_id):
    endpoint = f"{data_endpoint}{municipality_id}/kpi/{solar_kpi}"
    response = requests.get(endpoint)
    data = response.json()

    return data


def fetch_power_data():
    municipalities = fetch_municipalities()

    water_data = []
    solar_data = []

    for municipality in municipalities:
        municipality_id = municipality["id"]
        municipality_name = municipality["name"]

        water = fetch_water_data(municipality_id)["values"]
        for value in water:

            period = value["period"]
            value = value["values"][0]["value"]
            water_data.append({
                "name": municipality_name,
                "id": municipality_id,
                "power_type": "water",
                "period_year": period,
                "water_prod": value
            })

        solar = fetch_solar_data(municipality_id)
        for value in solar["values"]:
            period = value["period"]
            value = value["values"][0]["value"]
            solar_data.append({
                "name": municipality_name,
                "id": municipality_id,
                "power_type": "solar",
                "period_year": period,
                "solar_prod": value
            })
    return water_data, solar_data