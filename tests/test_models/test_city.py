#!/usr/bin/python3
"""Module to test the city class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """TestCity Class
    """
    def test_create_city(self):
        """Test when create a city
        """
        my_model = City()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'City')
