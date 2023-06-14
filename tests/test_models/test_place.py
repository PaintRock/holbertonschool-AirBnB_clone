"""test_place module"""
import unittest
from models.place import Place
import os
from models.base_model import BaseModel
import json


class TestPlace(unittest.TestCase):
    """TestPlace class documentation"""


    def setUp(self):
        """method to set up instance of Place/json file"""
        self.place = Place()
        
    def tearDown(self):
        """method to teardown instance of Place/json file"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        """method to check if instance intializes"""
        self.assertIsNotNone(self.place)
        
    def test_attr(self):
        
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertNotEqual(self.place.amenity_ids, "")
        self.place.save
    
if __name__ == '__main__':
    unittest.main()
