#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """User imports from BaseModel"""
    first_name = ""
    last_name = ""
    password = ""
    email = ""

    def to_json(self):
        """Return a JSON-serializable representation of the object"""
        json_dict = self.to_dict()
        json_dict['__class__'] = self.__class__.__name__
        return json_dict
