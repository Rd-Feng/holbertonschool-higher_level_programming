#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Functions to test max_integer"""
    def test_max_integer(self):
        """Testing max_integer function with different inputs"""
        #input not list
        #with self.assertRaises(TypeError):
        #    max_integer(5)
        #input None or list contains different type
        #with self.assertRaises(TypeError):
        #    max_integer(None)
        #    max_integer([1, 'a'])
        #no input
        self.assertEqual(max_integer(), None)
        #empty list
        self.assertEqual(max_integer([]), None)
        #input list with different elements
        self.assertEqual(max_integer([1, 2, 5, 4]), 5)
        #input list with repeated elements
        self.assertEqual(max_integer([3, 3, 2, 1, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()
