import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"


# funtion for read data 
def get_data(id = None):
    data = {}
    headers = {'content-Type':'application/json'}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

# get_data()


# post data

def post_data():
    data = {
        'name':'Rohsdan',
        'roll':129,
        'city':'ranchi'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

# post_data()




# update data

def update_data():
    data = {
        'id':3,
        'name':'raj',
        'roll':14,
        'city':'Dhandad'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
# update_data()




# delete data

def delete_data():
    data = {
      'id':4
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

delete_data()
    


