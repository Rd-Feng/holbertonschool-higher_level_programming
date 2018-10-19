#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle(3, 5)

    def test_id(self):
        self.assertEqual(self.rec.id, 1)

if __name__ == "__main__":
    unittest.main()
