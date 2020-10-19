import enum


class AnnouncementEnum(enum.Enum):
    available = 'Available'
    in_negotiation = 'In Negotiation'
    paid = 'Paid'
    delivered = 'Delivered'
    finished = 'Finished'

    @property
    def serialize(self):
        return self.value
