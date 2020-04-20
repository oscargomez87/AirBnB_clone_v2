#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of mySQL table
        name: input name
        cities: list of cities in state
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            Return:
            list of cities
            """
            list_cities = []
            all_cities = models.storage.all(City)
            for city_item in all_cities.items():
                if city_item[1].state_id == self.id:
                    list_cities.append(city_item[1])
            return list_cities
