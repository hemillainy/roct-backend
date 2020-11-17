import requests
import json


def read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def populate_team():
    team = read_json("team.json")
    headers = {
        'Content-Type': 'application/json',
    }
    url = 'http://geovanens.pythonanywhere.com/users'
    for user in team:
        data_ = json.dumps(user)
        response = requests.post(url, headers=headers, data=data_)
        print(response)
    login = json.dumps({
        "email": user["email"],
        "password": user["password"]
    })
    login_url = 'http://geovanens.pythonanywhere.com/auth/login'
    token = requests.post(login_url, headers=headers, data=login).json()['token']
    return token


def populate_items(token):
    items = read_json("items.json")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    url = 'http://geovanens.pythonanywhere.com/announcements/add'
    for item in items:
        data_ = json.dumps(item)
        response = requests.post(url, headers=headers, data=data_)
        print(response)
