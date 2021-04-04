from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Enum, String, Column
from .enums import PurchaseStatusEnum, TypeCard
from .user import User
from .announcement import Announcement


@dataclass
class Purchase(db.Model):
    __tablename__ = 'purchases'

    uuid = Column(Integer, primary_key=True)
    status = Column(Enum(PurchaseStatusEnum))
    announcement_uuid = Column(Integer)
    payment_uuid = Column(Integer)
    salesman_uuid = Column(Integer)
    buyer_uuid = Column(Integer)
    nick_game = Column(String(255))
    salesman_delivery_confirmation = Column(db.Boolean, default=False, nullable=False)
    buyer_delivery_confirmation = Column(db.Boolean, default=False, nullable=False)

    def __init__(self, announcement_uuid, salesman_uuid, buyer_uuid, nick_game):
        self.announcement_uuid = announcement_uuid
        self.status = PurchaseStatusEnum.initiated
        self.salesman_uuid = salesman_uuid
        self.buyer_uuid = buyer_uuid
        self.nick_game = nick_game
        self.salesman_delivery_confirmation = False
        self.buyer_delivery_confirmation = False

    @property
    def get_salesman(self):
        return User.query.filter_by(id=self.salesman_uuid).first().serialize()

    @property
    def get_buyer(self):
        return User.query.filter_by(id=self.buyer_uuid).first().serialize()

    @property
    def get_announcement(self):
        return Announcement.query.filter_by(uuid=self.announcement_uuid).first().serialize()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'uuid': self.uuid,
            'status': self.status.serialize,
            'announcement': self.get_announcement,
            'type_card': self.type_card.serialize,
            'number_card': self.number_card,
            'cpf_owner_card': self.cpf_owner_card,
            'validity_card': self.validity_card,
            'name_owner_card': self.name_owner_card,
            'salesman': self.get_salesman,
            'buyer': self.get_buyer,
            "nick_game": self.nick_game,
            "salesman_delivery_confirmation": self.salesman_delivery_confirmation,
            "buyer_delivery_confirmation": self.buyer_delivery_confirmation,
        }
