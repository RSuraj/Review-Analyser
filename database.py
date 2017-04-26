import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
class Webdata(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    review = Column(String(600), nullable=False)
    
engine = create_engine('sqlite:///info.db')


Base.metadata.create_all(engine)
