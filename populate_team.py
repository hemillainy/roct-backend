import requests
import json

import sys

amb = sys.argv[1]
print(amb)

#{"name": String, "email": String, "cpf": String, "phone": String, "isSalesman": Boolean, "password": String, "avatar": String}

data = [
    {
        "name":"Hemillainy Santos",
        "email":"hemillainysantos@gmail.com",
        "cpf":"14569872235",
        "phone":"88218483829",
        "isSalesman":False,
        "password":"hemi@123", 
        "avatar": "https://i.imgur.com/bEOnkfU.jpg"
    }
]

headers = {
    'Content-Type': 'application/json',
}

URL = 'https://roct-api.herokuapp.com/users' if amb=='prod' else 'http://localhost:5001/users'
for user in data:
    data_ = json.dumps(user)
    response = requests.post(URL, headers=headers, data=data_)
    print(response)
