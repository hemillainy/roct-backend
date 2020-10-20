from roct import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    nickname = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(255))
    cpf = db.Column(db.String(255), nullable=False, unique=True)
    is_salesman = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, name, nickname, phone, email, password, uuid, avatar, isSalesman, cpf):
        self.uuid = uuid
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.password = password
        self.avatar = avatar
        self.is_salesman = isSalesman
        self.cpf = cpf

    def serialize(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "phone": self.phone,
            "email": self.email,
            "avatar": self.avatar,
            "id": self.uuid,
            "isSalesman": self.is_salesman,
            "cpf": self.cpf
        }

