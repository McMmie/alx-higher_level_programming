#!/usr/bin/python3
"""
this is a module for the state class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    this is a class that inherits from the sqlalchemy
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
