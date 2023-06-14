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
        
     def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.amenity.name, "")
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.amenity), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.amenity.__str__())
    
def test_amenity(self):
    """Empty test"""
    pass

if __name__ == '__main__':
    unittest.main()
