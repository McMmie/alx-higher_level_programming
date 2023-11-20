#!/usr/bin/python3
"""
this is a module for the city class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    this is a city class that inherits from the sqlalchemy
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
