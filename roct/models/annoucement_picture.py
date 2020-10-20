from roct import db
from uuid import uuid4
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

class AnnouncementPicture(db.Model, Image):
    """Announcement picture model."""
    announcement_uuid = db.Column(UUID(as_uuid=True), ForeignKey('announcements.uuid'), primary_key=True, default=uuid4)
    announcement = relationship('Announcement')
    __tablename__ = 'announcement_picture'