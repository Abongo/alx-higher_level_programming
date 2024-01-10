#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of positive integers in a different order
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list containing zero
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a single-element list
        self.assertEqual(max_integer([42]), 42)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

        # Test with a list of floats
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

        # Test with a list containing a mix of integers and floats
        self.assertEqual(max_integer([1, 2, 3.5, 4]), 4)

if __name__ == '__main__':
    unittest.main()
