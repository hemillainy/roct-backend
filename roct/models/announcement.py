from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Enum, String, Float, Column, ForeignKey

from .enums import AnnouncementStatusEnum, AnnouncementTypeEnum


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

    def __init__(self, image, name, description, price, type_, salesman_uuid):
        self.image = image
        self.name = name
        self.description = description
        self.price = price
        self.status = AnnouncementStatusEnum.available
        self.type_ = AnnouncementTypeEnum[type_]
        self.salesman_uuid = salesman_uuid

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
            'salesman_uuid': self.salesman_uuid
        }
