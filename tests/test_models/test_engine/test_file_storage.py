#!/usr/bin/python3
"""Module to test file storage
"""
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestsFileStorage Class
    """

    def test_all(self):
        """Test when return objects
        """

        my_model = BaseModel()
        storage.new(my_model)
        self.assertEqual(type(storage.all()), dict)
