import pandas as pd
import requests
import json

api_key = "AIzaSyBnXFVBesNEcrS-N8yhXb1SHH9AvECS2cg"

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



#url = https://api.zippopotam.us/us/{state.lower()}/{city.lower()}

# for index, row in capitals.iterrows():
#     print(row['state'])

# dataDict = dict(capitals)

# for values in dataDict:
#     for i in range(len(dataDict['state'])):
#          city = dataDict['capital'][i].lower()
#          state = dataDict['abbrev'][i].lower()
#          print(city, state)

# df = pd.DataFrame(dataDict)
        
# for values in datalist:
#     for i in range(len(datalist['state'])):
#         print(datalist['capital'][i])

# url = "https://api.zippopotam.us/us/ma/belmont"

# results = requests.get(url).text
# results = json.loads(results)
# print(results['places'][0]['longitude'])
# print(results['places'][0]['latitude'])

for i, row in capitals.iterrows():
    city = row['capital'].lower()
    print(city)
