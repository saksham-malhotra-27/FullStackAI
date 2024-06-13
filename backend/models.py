from sqlalchemy import Column, String, Integer
from database import Base 
from datetime import datetime


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(String)
    filename = Column(String)