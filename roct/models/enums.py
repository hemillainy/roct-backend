import enum


class AnnouncementStatusEnum(enum.Enum):
    available = 'Available'
    in_negotiation = 'In Negotiation'
    paid = 'Paid'
    delivered = 'Delivered'
    finished = 'Finished'

    @property
    def serialize(self):
        return self.value


class AnnouncementTypeEnum(enum.Enum):
    item = 'Item'
    account = 'Account'
    gold = 'Gold'

    @property
    def serialize(self):
        return self.value
