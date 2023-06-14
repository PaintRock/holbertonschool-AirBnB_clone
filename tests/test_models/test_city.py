"""test_city module"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """TestCity class documentation"""


    def test_city(self):
        """Test to see if city is empty"""
        cityscape = city()
        self.assertIsNotEqual(cityscape.id, None)
        
    def test_state_id(self):
        """Test to see if state id is empty"""
        statescape = state_id()
        self.assertIsNotEqual(statescape.id, None)


if __name__ == '__main__':
    unittest.main()
