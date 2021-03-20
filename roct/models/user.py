from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Column, String
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    cpf = Column(String(255), nullable=False, unique=True)
    isSalesman = Column(db.Boolean, default=False, nullable=False)
    avatar = Column(String(255))
    isSuper = Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, phone, email, password, isSalesman, cpf, avatar, isSuper):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()
        self.avatar = avatar
        self.isSalesman = isSalesman
        self.cpf = cpf
        self.isSuper = isSuper

    def serialize(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "id": self.id,
            "isSalesman": self.isSalesman,
            "cpf": self.cpf,
            "avatar": self.avatar,
            "isSuper": self.isSuper
        }
