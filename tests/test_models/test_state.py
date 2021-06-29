#!/usr/bin/python3
"""Module to test the state class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """TestState Class
    """
    def test_create_state(self):
        """Test when create a state
        """
        my_model = State()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'State')
