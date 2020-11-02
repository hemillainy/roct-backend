# roct-backend

## Routes

    base - http://geovanens.pythonanywhere.com/

## Auth - /auth

    POST /auth/login            - login: {"email": String, "password": String}

## Users - /users

    POST /users                      - create new user: {"name": String, "email": String, "cpf": String, "phone": String, "isSalesman": Boolean, "password": String, "avatar": String}
    GET  /users/<id>                 - Get the user that has the id
    PUT  /users/<id>                 - Update the user that has the id

## Announcements - /announcements

    GET  /check                      - check if announcements endpoints live
    GET  /announcements              - get list of all announcements
    GET  /announcements/<uuid>       - get one announcement, need uiid announcement
    GET  /announcements/search/<var> - takes a list of announcement containing var in its name
    POST /announcements/add          - add new announcement - need body with image(url), name(string), description(string), price(float), type_({item, account, gold}), salesman_uuid(int)
