#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import environ

# Define Base class
Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(length=60), primary_key=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False,
                        default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """

        if kwargs:
            if "created_at" or "updated_at" not in kwargs.keys():
                self.created_at = self.updated_at = datetime.utcnow()
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        created = self.created_at
        updated = self.updated_at

        my_dict = dict(self.__dict__)
        my_dict["created_at"] = created.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = updated.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "_sa_instance_state" in my_dict.keys():
            del(my_dict["_sa_instance_state"])

        return my_dict

    def delete(self):
        """delete the current instance from the storage
        """
        models.storage.delete(self)
