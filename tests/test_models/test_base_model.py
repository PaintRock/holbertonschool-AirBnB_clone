"""test_base module"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review

class TestBaseModel(unittest.TestCase):
    """TestBase class documentation"""
    def test_init(self):
        """ Test initialization of BaseModel class """
        modelmodel = BaseModel()
        self.assertIsNotNone(modelmodel.id)

    def test_init2(self):
        """idk"""
        modelmodel = BaseModel()
        self.assertIsInstance(modelmodel.created_at, datetime)

    def test_init3(self):
        """updated_at belongs to datetime class"""
        modelmodel = BaseModel()
        self.assertIsInstance(modelmodel.updated_at, datetime)

    def test_init4(self):
        """created and updated"""
        modelmodel = BaseModel()
        self.assertEqual(modelmodel.created_at, modelmodel.updated_at)
    
    def test_save(self):
        """ test the save method of BaseModel class """
        fakemod = BaseModel()
        fakecreate = fakemod.created_at
        fakeupdate = fakemod.updated_at
        fakemod.save()
        self.assertEqual(fakemod.created_at, fakecreate)
        self.assertNotEqual(fakemod.updated_at, fakeupdate)

    def test_to_dict(self):
        gizelle = BaseModel()
        gizelle_dict = gizelle.to_dict()
        self.assertIsInstance(gizelle_dict, dict)
        self.assertIsInstance(gizelle_dict["updated_at"], str)
        self.assertIsInstance(gizelle_dict["created_at"], str)

    def test__str__(self):
        """Test the string representation of BaseModel instance"""
        review = Review()
        review.id = "123"
        review.user_id = "456"
        review.place_id = "789"
        review.text = "Test review"
    
        expected_str = "[Review] (123) {'id': '123', 'user_id': '456', 'place_id': '789', 'text': 'Test review'}"
        self.assertEqual(str(review), expected_str)

if __name__ == '__main__':
    unittest.main()
