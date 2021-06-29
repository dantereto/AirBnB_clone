#!/usr/bin/python3
"""Module to test the amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestAmenity Class
    """
    def test_create_amenity(self):
        """Test when create a amenity
        """
        my_model = Amenity()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Amenity')
