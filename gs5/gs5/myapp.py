import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"


# funtion for read data 
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    data = r.json()
    print(data)

# get_data()


# post data

def post_data():
    data = {
        'name':'rohit',
        'roll':22,
        'city':'ranchid'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)

post_data()




# update data

def update_data():
    data = {
        'id':5,
        'name':'aman',
        'roll':14,
        'city':'Dhandad'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)
# update_data()




# delete data

def delete_data():
    data = {
      'id':12
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)

# delete_data()
    


