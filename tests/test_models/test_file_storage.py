#!/usr/bin/python3
"""Module to test file storage
"""
import unittest
import  models
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestsFileStorage Class
    """
    # def test_new(self):
    #     """ Test whe a calss is created
    #     """
    #     my_model = BaseModel()
    #     storage.new(my_model)
    #     self.assertTrue('BaseModel.{}'.format(my_model.id) in models.storage.__objects.keys())

    # def test_all(self):
    #     """Test when return objects
    #     """
    #     my_model = BaseModel()
    #     storage.new(my_model)
    #     self.assertEqual(type(storage.all()), dict)
