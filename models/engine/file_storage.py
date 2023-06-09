#!/usr/bin/python3
"""
Serializes the Class instances to a JSON file.
"""
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime


class FileStorage:
    """ defines FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets obj in __objects with key/value pair """
        name = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        full_dict = {}
        for i in FileStorage.__objects.keys():
            full_dict[i] = FileStorage.__objects[i].to_json()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(full_dict))

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        reload_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                       "City": City, "Amenity": Amenity, "Place": Place,
                       "Review": Review}

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                reloaded = json.load(f)
                for obj, value in reloaded.items():
                    item_class = reloaded[obj].get("__class__")
                    if item_class in reload_dict:
                        cls_func = reload_dict.get(item_class)
                        FileStorage.__objects[obj] = cls_func(**reloaded[obj])

    def destroy_all(self):
        """ deletes all"""
        FileStorage.__objects.clear()
