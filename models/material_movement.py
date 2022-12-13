import Database.db as db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from datetime import datetime
import json


class MaterialMovement(db.Base):
    __tablename__ = 'material_movement'
    id = Column(String(250), primary_key=True)
    material_id = Column(String(250), ForeignKey("material.id"))
    quantity = Column(Integer())
    date = Column(DateTime(), default=datetime.now())
    movement_type = Column(String(250))

    def to_json(self):
        m = {'id': self.id, 'material_id': self.material_id, 'quantity': self.quantity, 'date': self.date,
             'movement_type': self.movement_type}
        return json.dumps(m, indent=4)
