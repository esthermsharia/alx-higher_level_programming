#!/usr/bin/python3
"""
Contains tests for the base class
"""

import unittest
import pep8
import inspect

from models import base
Base = base.Base

class TestBaseDocs(unittest.TestCase):
    """Contains tests for documentation and style of the Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the  tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the module docstring implementation"""
        self.assertTrue(len(base.__doc__) >= 1)

        def test_class_docstring(self):
            """Tests for the Base class docstring"""
            self.assertTrue(len(Base.__doc__) >= 1)

    def test_pep8_style__base(self):
        """Test that models/base.py conforms to PEP8."""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['models/base.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found pep8 style errors and warnings.")

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)
