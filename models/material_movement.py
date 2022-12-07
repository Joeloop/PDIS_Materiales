import Database.db as db
from sqlalchemy import Column, Integer, String, ForeignKey, Date


class MaterialMovement(db.Base):
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
