#!/usr/bin/python3

import pep8
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime, date


class TestBaseModel(unittest.TestCase):

    def test_cases(self):
        my_model = BaseModel()
        ids = uuid.UUID(my_model.id)
        self.assertIsInstance(ids, uuid.UUID)
        self.assertIsInstance(my_model.created_at, datetime)
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Check pep8")


if __name__ == '__main__':
    unittest.main()