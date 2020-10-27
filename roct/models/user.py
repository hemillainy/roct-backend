from roct import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID, Integer, Column, String
from flask_bcrypt import Bcrypt
from uuid import uuid4


bcrypt = Bcrypt()

@dataclass
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
        self.password = bcrypt.generate_password_hash(password).decode()
        self.avatar = avatar
    
