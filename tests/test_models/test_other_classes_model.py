#!/usr/bin/python3
"""Module to test the different classes
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review

from datetime import datetime, date


class TestClasses(unittest.TestCase):
    """TestClasses class
    """
    def test_create_classes(self):
        """When create a class
        """

        my_model = User()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'User')
        my_model = City()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'City')
        my_model = Place()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Place')
        my_model = State()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'State')
        my_model = Review()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Review')
        my_model = Amenity()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Amenity')
        my_model = BaseModel()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'BaseModel')
