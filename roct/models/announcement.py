from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Enum, String, Float, Column, ForeignKey, DateTime
import datetime
from .enums import AnnouncementStatusEnum, AnnouncementTypeEnum
from .user import User


@dataclass
class Announcement(db.Model):
    __tablename__ = 'announcements'

    uuid = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    status = Column(Enum(AnnouncementStatusEnum))
    type_ = Column(Enum(AnnouncementTypeEnum))
    salesman_uuid = Column(Integer)
    game = Column(String(255))
    server = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, image, name, description, price, type_, salesman_uuid, server, game="wyd"):
        self.image = image
        self.name = name
        self.description = description
        self.price = price
        self.status = AnnouncementStatusEnum.available
        self.type_ = AnnouncementTypeEnum[type_]
        self.salesman_uuid = salesman_uuid
        self.server = server
        self.game = game

    @property
    def get_user(self):
        return User.query.filter_by(id=self.salesman_uuid).first().serialize()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'uuid': self.uuid,
            'image': self.image,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'status': self.status.serialize,
            'type_': self.type_.serialize,
            'salesman': self.get_user,
            'game': self.game,
            'server': self.server,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
