#!/usr/bin/python3
"""
    The unittest module to test for all functionalities
    associated with the TestBaseModel class and its
    subclasses.
"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """The main class for conducting tests."""
    def setUp(self):
        self.m1 = BaseModel()
        self.m2 = BaseModel()

    def test_uuid(self):
        """Test `uuid` instance variable."""
        self.assertIsInstance(self.m1, BaseModel)
        self.assertTrue(hasattr(self.m1, "id"))
        self.assertNotEqual(self.m1.id, self.m2.id)
        self.assertIsInstance(self.m1.id, str)

    def test_created_at(self):
        """Test `created_at` instance variable."""
        self.assertTrue(hasattr(self.m1, "created_at"))
        self.assertIsInstance(self.m1.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test `updated_at` instance variable."""
        self.assertTrue(hasattr(self.m1, "updated_at"))
        self.assertIsInstance(self.m1.updated_at, datetime.datetime)
