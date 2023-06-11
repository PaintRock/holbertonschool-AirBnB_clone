#!/usr/bin/python3
"""This module contains the class for file storage"""
import json
import models
from models.base_model import BaseModel


class FileStorage:
    """ Defines FileStorage class """

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ Returns __objects """
        return self.__objects

    def new(self, obj):
        """ Sets obj in __objects with key/value pair """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        full_dict = {}
        for i in self.__objects.keys():
            full_dict[i] = self.__objects[i].to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(full_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)

    except FileNotFoundError:
        pass
    except json.decoder.JSONDecodeError:
        pass
