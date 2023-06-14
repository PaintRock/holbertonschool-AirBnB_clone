#!/usr/bin/python3
"""Module for city"""
from models.base_model import BaseModel


class City(BaseModel):
    """City and state id"""
    state_id = ""
    name = ""

    def to_json(self):
        """Return a JSON-serializable representation of the object"""
        json_dict = self.to_dict()
        json_dict['__class__'] = self.__class__.__name__
        return json_dict
