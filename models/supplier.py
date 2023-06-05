from sqlalchemy import Column, Integer, String
from config.database import Base

class Supplier(Base):

    __tablename__ = "supplier"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)