#!/usr/bin/python3
"""This is the file DBStorage class for AirBnB
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models import User, State, City, Amenity, Place, Review
from models.base_model import Base


class DBStorage:
    """This class
    Attributes:
        __engine: conection to data base
        __session: session in data base
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instance of DBStorage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ.get('HBNB_MYSQL_USER'),
                                              environ.get('HBNB_MYSQL_PWD'),
                                              environ.get('HBNB_MYSQL_HOST'),
                                              environ.get('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if environ.get('HBNB_ENV') == "test":
            self.__engine.drop_all()

    def all(self, cls=None):
        """List all data in table
        Arguments:
            cls: input class
        Return:
            dictionary
        """
        objs_dict = {}
        objs = []
        all_objs = [User, State, City, Amenity, Place, Review]
        if cls:
            objs = self.__session.query(globals()[cls]).all()
        else:
            objs = self.__session.query(all_objs).all()
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """Add the object to the current database session
        Argument:
            obj: input object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is not None:
            pass

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        Session.configure(expire_on_commit=False)
        self.__session = Session()