import json
import requests

# this file is client frontend data store


# deserialization data json into string convert.

# # # create student
URL = "http://127.0.0.1:8000/create/"


def add_data():
    data = {
        'name': 'dhruv',
        'roll': 103,
        'city': 'Ahmedabad'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


url = "http://127.0.0.1:8000/Api/"

# get , update and delete data
def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)
    return data


# get_data(2)

def update_data():
    data = {
        'id': 1,
        'name': 'news',
        'roll': 102,
        'city': 'baroda'
    }

    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)


# update_data()

def delete_data():
    data = {
        'id': 10,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)


# delete_data()
