#!/usr/bin/python3
"""Place from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_json(self):
        """Return a JSON-serializable representation of the object"""
        json_dict = self.to_dict()
        json_dict['__class__'] = self.__class__.__name__
        return json_dict
