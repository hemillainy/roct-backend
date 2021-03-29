from roct import db
from dataclasses import dataclass
from sqlalchemy import Integer, Enum, String, Column

@dataclass
class Payment(db.Model):
    __tablename__ = 'payments'

    uuid = Column(Integer, primary_key=True)
    authorization_id = Column(String(255))
    payment_url = Column(String(255))
    qrcode = Column(String(255))
    reference_id = Column(String(255))

    def __init__(self, payment_url, qrcode, reference_id):
        self.authorization_id = ''
        self.payment_url = payment_url
        self.qrcode = qrcode
        self.reference_id = reference_id

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'uuid': self.uuid,
            'authorization_id': self.authorization_id,
            'payment_url': self.payment_url,
            'qrcode': self.qrcode
        }