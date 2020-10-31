# roct-backend

## Routes

    base - http://geovanens.pythonanywhere.com/

## Auth - /auth

    POST /auth/login                 - login to the system: {"email": String, "password": String}
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.     eyJpYXQiOjE2MDQwOTE2MDIsIm5iZiI6MTYwNDA5MTYwMiwianRpIjoiYmM4MTFhNzMtN2U1Yy00M2NmLWI0ZWEtYmVmYjQ4ZGQxY2EyIiwiZXhwIjoxNjA0MDkyNTAyLCJpZGVudGl0eSI6e30sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.1XXcquwHJZ0xYOai2NC0NVPA9vMzPM2W4MYct-CdM50"
    }

## Users - /users

    POST /users                      - create new user: {"name": String, "email": String, "cpf": String, "phone": String, "isSalesman": Boolean, "password": String, "nickname": String, "pwd": Object({"password": String, "confirm_password": String}, "avatar": String}
    GET  /users/<id>                 - Get the user that has the id
    PUT  /users/<id>                 - Update the user that has the id

## Announcements - /announcements

    GET  /check                      - check if announcements endpoints live
    GET  /announcements              - get list of all announcements
    GET  /announcements/<uuid>       - get one announcement, need uiid announcement
    GET  /announcements/search/<var> - takes a list of announcement containing var in its name
    POST /announcements/add          - add new announcement - need body with image(url), name(string), description(string), price(float), type_({item, account, gold}), salesman_uuid(int)
