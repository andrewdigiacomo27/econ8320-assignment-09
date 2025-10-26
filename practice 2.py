import pandas as pd
import json
import plotly.express as px
import requests

capitals = pd.DataFrame([["Alabama","Montgomery","AL"],
["Alaska","Juneau","AK"],
["Arizona","Phoenix","AZ"],
["Arkansas","Little Rock","AR"],
["California","Sacramento","CA"],
["Colorado","Denver","CO"],
["Connecticut","Hartford","CT"],
["Delaware","Dover","DE"],
["Florida","Tallahassee","FL"],
["Georgia","Atlanta","GA"],
["Hawaii","Honolulu","HI"],
["Idaho","Boise","ID"],
["Illinois","Springfield","IL"],
["Indiana","Indianapolis","IN"],
["Iowa","Des Moines","IA"],
["Kansas","Topeka","KS"],
["Kentucky","Frankfort","KY"],
["Louisiana","Baton Rouge","LA"],
["Maine","Augusta","ME"],
["Maryland","Annapolis","MD"],
["Massachusetts","Boston","MA"],
["Michigan","Lansing","MI"],
["Minnesota","Saint Paul","MN"],
["Mississippi","Jackson","MS"],
["Missouri","Jefferson City","MO"],
["Montana","Helena","MT"],
["Nebraska","Lincoln","NE"],
["Nevada","Carson City","NV"],
["New Hampshire","Concord","NH"],
["New Jersey","Trenton","NJ"],
["New Mexico","Santa Fe","NM"],
["New York","Albany","NY"],
["North Carolina","Raleigh","NC"],
["North Dakota","Bismarck","ND"],
["Ohio","Columbus","OH"],
["Oklahoma","Oklahoma City","OK"],
["Oregon","Salem","OR"],
["Pennsylvania","Harrisburg","PA"],
["Rhode Island","Providence","RI"],
["South Carolina","Columbia","SC"],
["South Dakota","Pierre","SD"],
["Tennessee","Nashville","TN"],
["Texas","Austin","TX"],
["Utah","Salt Lake City","UT"],
["Vermont","Montpelier","VT"],
["Virginia","Richmond","VA"],
["Washington","Olympia","WA"],
["West Virginia","Charleston","WV"],
["Wisconsin","Madison","WI"],
["Wyoming","Cheyenne","WY"]], columns = ['state', 'capital', 'abbrev'])

dataDict = dict(capitals)

longitude = []
latitude = []

for i, row in capitals.iterrows():
    city = row['capital'].lower()
    state = row['abbrev'].lower()

    url = f"https://api.zippopotam.us/us/{state}/{city}"

    results = requests.get(url).text
    results = json.loads(results)
    longitude.append(results['places'][0]['longitude'])
    latitude.append(results['places'][0]['latitude'])

capitals["long"] = longitude
capitals["lat"] = latitude
