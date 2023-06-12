#!/usr/bin/python3
"""This module contains the class for file storage"""
import uuid
import json
import models
from models.review import Review
from models.place import Place
from models. user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """ Defines FileStorage class """

    __file_path = "file.json"
    __objects = {}

    @classmethod
    def delete_all(cls):
        """removes all objects"""
        cls.__objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.loads(file.read())
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
