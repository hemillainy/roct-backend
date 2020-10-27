from roct import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy import Integer, Column, String
from flask_bcrypt import Bcrypt
from uuid import uuid4


bcrypt = Bcrypt()


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False, unique=True)
    phone = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    cpf = Column(String(255), nullable=False, unique=True)
    is_salesman = Column(db.Boolean, default=False, nullable=False)
    avatar = Column(String(255), nullable=False)

    def __init__(self, name, nickname, phone, email, password, isSalesman, cpf, avatar):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()
        self.avatar = avatar
        self.is_salesman = isSalesman
        self.cpf = cpf

    def serialize(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "phone": self.phone,
            "email": self.email,
            "id": self.id,
            "isSalesman": self.is_salesman,
            "cpf": self.cpf,
            "avatar": self.avatar
        }
