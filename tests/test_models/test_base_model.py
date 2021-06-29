#!/usr/bin/python3
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


if __name__ == '__main__':
    unittest.main()
