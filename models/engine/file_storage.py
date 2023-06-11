#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json
from datetime import datetime


class FileStorage:
    """ defines FileStorage class """

    __file_path = "./file.json"
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
