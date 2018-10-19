#!/usr/bin/python3
"""Test methods in Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test class Base"""

    def test_init(self):
        """test constructor"""
        self.assertEqual(Base(98).id, 98)
        self.assertEqual(Base('str_id').id, 'str_id')
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base().id, Base._Base__nb_objects)
        self.assertEqual(Base(None).id, Base._Base__nb_objects)
        with self.assertRaises(TypeError):
            Base(dne='this variable does not exist')
        with self.assertRaises(TypeError):
            Base(1, 2, 3)

    def test_from_json_string(self):
        """test from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{"1": "one"}]'),
                         [{'1': 'one'}])
        with self.assertRaises(ValueError):
            Base.from_json_string('some string cannot be decoded')
        with self.assertRaises(TypeError):
            Base.from_json_string(123)
        with self.assertRaises(TypeError):
            Base.from_json_string([1, 2])
        with self.assertRaises(TypeError):
            Base.from_json_string((1, 2))
        with self.assertRaises(TypeError):
            Base.from_json_string({'1': 'one'})
        with self.assertRaises(TypeError):
            Base.from_json_string(True)
        with self.assertRaises(TypeError):
            Base.from_json_string(1.2)
        with self.assertRaises(TypeError):
            Base.from_json_string(float('inf'))
        with self.assertRaises(TypeError):
            Base.from_json_string(float('nan'))

    def test_to_json_string(self):
        """test to_json_string
        This test convert object to string and convert back to object
        to see if an object is correctly converted to json string"""
        l_none, l0 = None, []
        l1 = [{'1': 'one', '2': 'two'}]
        l2 = [{'1': 'one'}, {'2': [2]}]
        newObj = Base.from_json_string(Base.to_json_string(l_none))
        self.assertEqual([], newObj)
        newObj = Base.from_json_string(Base.to_json_string(l0))
        self.assertEqual(l0, newObj)
        newObj = Base.from_json_string(Base.to_json_string(l1))
        self.assertEqual(l1, newObj)
        newObj = Base.from_json_string(Base.to_json_string(l2))
        self.assertEqual(l2, newObj)

    def test_save_to_file(self):
        """test save_to_file
        will be tested in derived classes"""
        pass

    def test_create(self):
        """test create
        will be tested in derived classes"""
        pass

    def test_load_from_file(self):
        """test load_from_file
        will be tested in derived classes"""
        pass

if __name__ == "__main__":
    unittest.main()
