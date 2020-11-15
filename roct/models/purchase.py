from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Enum, String, Column
from .enums import PurchaseStatusEnum, TypeCard
from .user import User


@dataclass
class Purchase(db.Model):
    __tablename__ = 'purchases'

    uuid = Column(Integer, primary_key=True)
    status = Column(Enum(PurchaseStatusEnum))
    announcement_uuid = Column(Integer)
    type_card = Column(Enum(TypeCard))
    number_card = Column(String(255))
    cvv = Column(String(3))
    cpf_owner_card = Column(String(255))
    validity_card = Column(String(255))
    name_owner_card = Column(String(255))
    salesman_uuid = Column(Integer)
    buyer_uuid = Column(Integer)
    nick_game = Column(String(255))

    def __init__(self, announcement_uuid, type_card, number_card, cvv, cpf_owner_card,
                 validity_card, name_owner_card, salesman_uuid, buyer_uuid, nick_game):
        self.announcement_uuid = announcement_uuid
        self.status = PurchaseStatusEnum.initiated
        self.type_card = TypeCard[type_card]
        self.number_card = number_card
        self.cvv = cvv
        self.cpf_owner_card = cpf_owner_card
        self.validity_card = validity_card
        self.name_owner_card = name_owner_card
        self.salesman_uuid = salesman_uuid
        self.buyer_uuid = buyer_uuid
        self.nick_game = nick_game

    @property
    def get_salesman(self):
        return User.query.filter_by(id=self.salesman_uuid).first().serialize()

    @property
    def get_buyer(self):
        return User.query.filter_by(id=self.buyer_uuid).first().serialize()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'uuid': self.uuid,
            'status': self.status.serialize,
            'announcement_uuid': self.announcement_uuid,
            'type_card': self.type_card.serialize,
            'number_card': self.number_card,
            'cpf_owner_card': self.cpf_owner_card,
            'validity_card': self.validity_card,
            'name_owner_card': self.name_owner_card,
            'salesman': self.get_salesman,
            'buyer': self.get_buyer,
            "nick_game": self.nick_game,
        }
