#!/usr/bin/python3
"""Module for unittest for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test class for 'base' module
    """
    def setUp(self):
        """Includes the function to be tested
        """
        Base._Base__nb_objects = 0

    def test_id_no_arg(self):
        """Test no argument(default)
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """Test with id set
        """
        b = Base(1234)
        self.assertEqual(b.id, 1234)

    def test_id_multiple_instance(self):
        """Test multiple instances without arg
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 5)

    def test_id_multiple_instance_with_id_arg(self):
        """Test multiple instances with arg
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(1234)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 1234)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)

    def test_id_str_arg(self):
        """Test multiple instances without arg
        """
        b1 = Base('1234')
        self.assertEqual(b1.id, '1234')
    
    def test_id_multiple_arg(self):
        """Test multiple arg
        """
        with self.assertRaises(TypeError):
            b = Base(1, 3)
    
    def test_access_private_attribute(self):
        """Test accessing private class attribute
        """
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

if __name__ == '__main__':
    unittest.main()
