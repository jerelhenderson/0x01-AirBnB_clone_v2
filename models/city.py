#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
import models
import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities", cascade="delete")
