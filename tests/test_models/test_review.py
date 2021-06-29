#!/usr/bin/python3
"""Module to test the review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview Class
    """
    def test_create_review(self):
        """Test when create a review
        """
        my_model = Review()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Review')
