import Database.db as db
from sqlalchemy import Column, Integer, String


class Material(db.Base):
    __tablename__ = 'material'
    id = Column(String(), primary_key=True, )
    name = Column(String(250))
    quantity = Column(Integer())
    unit_price = Column(Integer())

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit_price': self.unit_price
        }
