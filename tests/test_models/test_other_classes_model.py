#!/usr/bin/python3
"""Module to test the different classes
"""
import unittest
from models.base_model import BaseModel
from models.user import User
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

        my_model = BaseModel()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'BaseModel')
