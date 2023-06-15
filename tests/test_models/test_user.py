"""test_user module"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
import json

class TestUser(unittest.TestCase):
    """TestUser class documentation"""


    def setUp(self):
        """method to set up instance of User/json file"""
        self.user = User()
        
    def tearDown(self):
        """method to teardown instance of User/json file"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        """method to check if instance intializes"""
        self.assertIsNotNone(self.user)
        
    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertNotTrue(self.user.first_name, "")
        self.assertTrue(self.user.last_name, "")
        
if __name__ == '__main__':
    unittest.main()
  