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
        self.assertIsNotNone(self.review)
    
    def test__repr__(self):
        """method to print attributes of dictionary"""
        self.assertIsNotNone(self.review.__str__())

    def test_attr(self):
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.text, "")
    
    def test__str__(self):
    """Test the string representation of BaseModel instance"""
    review = Review()
    review.id = "123"
    review.user_id = "456"
    review.place_id = "789"
    review.text = "Test review"
    
    expected_str = "[Review] (123) {
        'id': '123', 'user_id': '456', 'place_id': '789', 'text': 'Test review'
        }"
    self.assertEqual(str(review), expected_str)
        
   
if __name__ == '__main__':
    unittest.main()
