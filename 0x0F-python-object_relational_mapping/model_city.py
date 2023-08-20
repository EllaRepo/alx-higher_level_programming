#!/usr/bin/python3
"""Python file that contains the class definition of a
   City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
   """class definition of city
   """
   __tablename__ = 'cities'
   id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
   name = Column(String(128), nullable=False)
   state_id = Column(Integer, ('states.id'), nullable=False)
