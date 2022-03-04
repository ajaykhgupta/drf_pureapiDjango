"""
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

"""

import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data(5)

def post_data():
    data = {
        'name':'Sonali',
        'roll':50,
        'city':'Bandra'
    }
    headers = {'content-Type': 'application/json'}
    # dumps python to json
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# post_data()


def update_data():
    data ={
        'id':5,
        'name':'Jack',
        'city' : 'Ranchi'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {'id' : 5}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.delete(url=URL, headers=headers ,data=json_data)
    data = r.json()
    print(data)

delete_data()