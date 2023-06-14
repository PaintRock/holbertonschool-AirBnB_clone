"""test_state module"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State
import json

class TestAmenity(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of State/json file'''
        self.state = State()

    def tearDown(self):
        '''method to tear down instance of State/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.state)
        
if __name__ == '__main__':
    unittest.main()
