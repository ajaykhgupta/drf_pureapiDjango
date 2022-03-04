import requests
import json

''' This is client side application'''

URL = "http://127.0.0.1:8000/stucreate/"
# data is in dictionary 
data = {
    'name' : 'Alex',
    'roll': '200',
    'city':'bhopal'
}

# convert data to json (python to json so use dumps)

json_data = json.dumps(data)

r  = requests.post(url = URL, data=json_data)

data = r.json()
print(data)
