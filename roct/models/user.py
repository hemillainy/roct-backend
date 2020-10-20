from roct import db
from sqlalchemy import Integer, Column, String


class User(db.Model):
    __tablename__ = 'users'

    uuid = Column(Integer, primary_key=True)
    name = Column(String(255))
    nickname = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    avatar = Column(String(255))

    def __init__(self, name, nickname, phone, email, password, avatar):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.password = password
        self.avatar = avatar
