from roct import db
from dataclasses import dataclass

class User(db.Model):
    __tablename__ = 'users'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # avatar =

    def __init__(self, name, nickname, phone, email, password):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.password = password
    