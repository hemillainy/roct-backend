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


class PurchaseStatusEnum(enum.Enum):
    initiated = 'Iniciada'
    paid = 'Item pago, aguardando entrega'
    delivered = 'Item entregue, aguardando confirmação'
    finished = 'Finalizada'

    @property
    def serialize(self):
        return self.value


class TypeCard(enum.Enum):
    credit = "Crédito"
    debit = "Débito"

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
