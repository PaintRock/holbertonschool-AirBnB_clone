#!/usr/bin/python3
"""Class that defines all the common attributes/methods for
the other classes"""
import uuid
from datetime import datetime
import models
make_time = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, make_time)
            self.updated_at = datetime.strptime(self.updated_at, make_time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)