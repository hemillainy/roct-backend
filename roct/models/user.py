from roct import db
from dataclasses import dataclass
from sqlalchemy import String, Column, Boolean, Integer


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    nickname = Column(String(255), nullable=False, unique=True)
    phone = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    cpf = Column(String(255), nullable=False, unique=True)
    is_salesman = Column(Boolean(), default=False, nullable=False)

    def __init__(self, name, nickname, phone, email, password, isSalesman, cpf, avatar):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.password = password
        self.is_salesman = isSalesman
        self.cpf = cpf
        self.avatar = avatar

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
