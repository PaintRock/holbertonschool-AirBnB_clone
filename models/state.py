#!/usr/bin/python3
"""AirBnB State class from BaseModel"""
from models.base_model import BaseModel
import json

class State(BaseModel):
    """State class from BaseModel"""
    name = ""

    def to_json(self):
        """Return a JSON-serializable representation of the object"""
        json_dict = self.to_dict()
        json_dict['__class__'] = self.__class__.__name__
        return json_dict
