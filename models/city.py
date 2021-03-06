#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        state = relationship("State", foreign_keys=[state_id],
                             back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete, delete-orphan")
