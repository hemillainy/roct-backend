# roct-backend

## Routes
## Users - 
    GET
## Announcements - /announcements
    GET  /check                      - check if announcements endpoints live
    GET  /announcements              - get list of all announcements
    GET  /announcements/<uuid>       - get one announcement, need uiid announcement
    GET  /announcements/search/<var> - takes a list of announcement containing var in its name
    POST /announcements/add          - add new announcement - need body with image(url), name(string), description(string), price(float), type_({item, account, gold}), salesman_uuid(int)
    
    
    
    
    
