import requests
import json

import sys

amb = sys.argv[1]
print(amb)

#{"name": String, "email": String, "cpf": String, "phone": String, "isSalesman": Boolean, "password": String, "avatar": String}

data = [
    {
        "name":"cassio",
        "email":"cassio@cassio.com",
        "cpf":"12345667895",
        "phone":"87218483828",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/ggCISwp.jpg"
    },
    {
        "name":"geovane",
        "email":"geovane@geovane.com",
        "cpf":"31041952007",
        "phone":"55743707006",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/1XlJf0v.jpg"
    },
    {
        "name":"vinicius",
        "email":"vini@vini.com",
        "cpf":"77645024054",
        "phone":"22210663083",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/unOYgBb.jpg"
    },
    {
        "name":"hemilliany",
        "email":"hemi@hemi.com",
        "cpf":"68224055000",
        "phone":"68969244034",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/bEOnkfU.jpg"
    },
    {
        "name":"gabriel",
        "email":"biel@biel.com",
        "cpf":"32323144065",
        "phone":"74715161001",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/U4OLrM4.jpg"
    },
    {
        "name":"bruno",
        "email":"bruno@bruno.com",
        "cpf":"56208085055",
        "phone":"29188319059",
        "isSalesman":False,
        "password":"abc", 
        "avatar": "https://i.imgur.com/hGeSKvw.jpg"
    }
]

headers = {
    'Content-Type': 'application/json',
}

URL = 'http://geovanens.pythonanywhere.com/users' if amb=='prod' else 'http://localhost:5001/users'
for user in data:
    data_ = json.dumps(user)
    response = requests.post(URL, headers=headers, data=data_)
    print(response)
