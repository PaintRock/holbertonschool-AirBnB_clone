"""test_amenity module"""
import unittest
from models.amenity import Amenity
import os
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """TestAmenity class documentation"""

    def setUp(self):
        """method to set up instance of Amenity/json file"""
        self.amenity = Amenity()

    def tearDown(self):
        """method to tear down instance of Amenity/json file"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.amenity) 
          
if __name__ == '__main__':
    unittest.main()
