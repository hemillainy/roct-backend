from roct import db
from uuid import uuid4
from sqlalchemy import ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from .annoucement_picture import AnnouncementPicture

@dataclass
class Announcement(db.Model):
    __tablename__ = 'announcements'
    
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # image = image_attachment('AnnouncementPicture')
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    # salesman = type salesman
    #status = 

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'uuid': self.uuid,
           'name': self.name,
           'description': self.description,
           'price': self.price
       }
