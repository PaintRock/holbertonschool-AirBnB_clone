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
        '''method to tear down instance of Review/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.review) 
        
    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.review.name, "")
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "id"))
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.review), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.review.__str__())  
    
    def test_review(self):
        """Empty test"""
        pass

if __name__ == '__main__':
    unittest.main()
