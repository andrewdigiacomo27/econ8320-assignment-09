import json
import requests
import pandas as pd

destinations = [
    'Omaha, NE',
    'San Diego, CA',
    'Santa Fe, NM',
    'Chicago, IL',
    'Seattle, WA'
]

origin = "Washington, DC"

def travel_time(orgin, dest, api_key):

    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    url += f"?destinations={dest}"
    url += f"&origins={origin}"
    url += f"&key={api_key}"

    results = requests.get(url).text
    results = json.loads(results) #turns into dictionary

    travel_time = results['rows'][0]['elements'][0]['value']

    return travel_time

def travel_table(origin, dest):
    api_key = "AIzaSyBnXFVBesNEcrS-N8yhXb1SHH9AvECS2cg"

    data = []

    for location in destinations:
        row = []
        row.append(location)
        row.append(travel_time(origin, location, api_key))

        data.append(row)

    data = pd.DataFrame(data, columns = 'destination', 'travel_time')

    return data

data = travel_table(origin, destinations)