#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class for '6-max_integer' module
    """
    def setUp(self):
        """Includes the function to be tested
        """
        self.max_integer = max_integer

    def test_empty_list(self):
        """Test empty list
        """
        self.assertEqual(self.max_integer([]), None)

    def test_max_at_start(self):
        """Test for a list with the maximum integer at the beiginning
        """
        self.assertEqual(self.max_integer([245, 123, 34, 67]), 245)

    def test_max_at_middle(self):
        """Test for a list with the maximum integer at the middle
        """
        self.assertEqual(self.max_integer([245, 123, 1689, 34, 67]), 1689)

    def test_max_at_end(self):
        """Test for a list with the maximum integer at the end
        """
        self.assertEqual(self.max_integer([245, 123, 168, 34, 676743]), 676743)

    def test_one_negative(self):
        """Test for a list with one negative integer in the list
        """
        self.assertEqual(self.max_integer([245, -123, 1689, 34, 67]), 1689)

    def test_all_negative(self):
        """Test for a list with the all integers being negative
        """
        self.assertEqual(self.max_integer([-245, -123, -1689, -34, -67]), -34)

    def test_only_one_number_in_list(self):
        """Test for a list with only one number
        """
        self.assertEqual(self.max_integer([245]), 245)


if __name__ == '__main__':
    unittest.main()
