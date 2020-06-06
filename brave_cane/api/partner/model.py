from sqlalchemy import Column, Integer, String, JSON

from brave_cane.database import Base, Model


class Partner(Model):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tradingName = Column(String(244), nullable=False, index=True, unique=True)
    ownerName = Column(String(244))
    document = Column(String(244))
    coverageArea = Column(JSON())