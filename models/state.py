#!/usr/bin/python3
"""State Module for HBNB project."""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """State class."""

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        kwargs = {"cascade": "all, delete-orphan", "backref": "state"}
        cities = relationship("City", **kwargs)
    else:
        name = ""

        @property
        def cities(self):
            """Return list of Cities with the current state_id."""
            all_cities = models.storage.all(City)
            lt_cities = []
            for key, value in all_cities.items():
                if value.state_id == self.id:
                    lt_cities.append(value)
            return lt_cities
