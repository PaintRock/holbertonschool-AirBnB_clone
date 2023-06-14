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

    def test_place():
    """Empty test"""
    pass
        pass
    
if __name__ == '__main__':
    unittest.main()
