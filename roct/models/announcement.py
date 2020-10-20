from roct import db
import uuid
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import Integer, Enum, String, Float, Column

from .enums import AnnouncementStatusEnum, AnnouncementTypeEnum


@dataclass
class Announcement(db.Model):
    __tablename__ = 'announcements'

    uuid = Column(Integer, primary_key=True)
    # image = image_attachment('AnnouncementPicture')
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    status = Column(Enum(AnnouncementStatusEnum))
    # salesman = type salesman
    type_ = Column(Enum(AnnouncementStatusEnum))

    def __init__(self, name, description, price, type_):
        self.name = name
        self.description = description
        self.price = price
        self.status = AnnouncementStatusEnum.available
        self.type_ = AnnouncementStatusEnum[type_]

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'uuid': self.uuid,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'status': self.status.serialize
        }
