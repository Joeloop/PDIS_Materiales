from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship

import os

Base = declarative_base()


class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True)
    name = Column(Date)
    quantity = Column(Date)
    unit_price = Column(Integer)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit_price': self.unit_price
        }


class MaterialMovement(Base):
    __tablename__ = 'material_movement'
    id = Column(Integer, primary_key=True)
    material_id = Column(String(250), ForeignKey("material.id"))
    quantity = Column(String(250))
    date = Column(Date)
    movement_type = Column(String(250))

    def to_json(self):
        return {
            'id': self.id,
            'material_id': self.material_id,
            'quantity': self.quantity,
            'date': self.date,
            'movement_type': self.movement_type
        }


path = os.path.dirname(os.path.abspath("tables.py"))
connection = f"sqlite:///{path}/database.db"
engine = create_engine(connection)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
