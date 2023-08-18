#!/usr/bin/python3
"""Define the City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    """Represent the City class"""

    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True,
            primary_key=True, autoincrement=True)
    name = Column(string(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
