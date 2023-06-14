"""test_state module"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State
import json

class TestState(unittest.TestCase):

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
        
     def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.state.name, "")
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "id"))
        self.city.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.state), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.state.__str__())
        
if __name__ == '__main__':
    unittest.main()
