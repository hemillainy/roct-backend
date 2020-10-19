from roct import db
from uuid import uuid4
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import Integer, Enum, String, Float, Column

from .announcement_status import AnnouncementEnum


@dataclass
class Announcement(db.Model):
    __tablename__ = 'announcements'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # image = image_attachment('AnnouncementPicture')
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    status = Column(Enum(AnnouncementEnum))
    # salesman = type salesman

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.status = AnnouncementEnum.available

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
