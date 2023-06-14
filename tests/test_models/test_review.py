"""test_review module"""
import unittest
from models.review import Review
import os
from models.base_model import BaseModel
import json

class TestReview(unittest.TestCase):
    """TestReview class documentation"""


    def setUp(self):
        '''method to set up instance of Review/json file'''
        self.review = Review()

    def tearDown(self):
        """method to tear down instance of Review/json file"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass
    
    def test___init__(self):
        """method to check if instance intializes"""
        self.assertIsNotNone(self.place)  
    
    def test__repr__(self):
        """method to print attributes of dictionary"""
        self.assertIsNotNone(self.review.__str__())  

if __name__ == '__main__':
    unittest.main()
