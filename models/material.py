import Database.db as db
from sqlalchemy import Column, Integer, String


class Material(db.Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(250))
    quantity = Column(Integer)
    unit_price = Column(Integer)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit_price': self.unit_price
        }

    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
