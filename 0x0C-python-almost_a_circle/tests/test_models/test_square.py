#!/usr/bin/python3
"""test square module"""
import unittest
import io
import sys
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """test Square class"""

    def test_init_error(self):
        """test init"""
        with self.assertRaises(TypeError) as e:
            Square('abc')
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as e:
            Square(-2)
        self.assertEqual(str(e.exception), 'width must be > 0')
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_init_success(self):
        """test init success case"""
        s = Square(2)
        self.assertEqual(s.__dict__.get('size'), None)
        self.assertEqual((s.size, s.x, s.y, s.id),
                         (2, 0, 0, s._Base__nb_objects))
        s = Square(2, 1, 2, id=89)
        self.assertEqual((s.size, s.x, s.y, s.id),
                         (2, 1, 2, 89))

    def test_size(self):
        """test size setter and getter"""
        s = Square(3)
        self.assertEqual(s.size, 3)
        s.size = 5
        self.assertEqual(s.size, 5)
        self.assertEqual((s._Rectangle__width, s._Rectangle__height), (5, 5))
        with self.assertRaises(TypeError) as e:
            s.size = '123'
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as e:
            s.size = 0
        self.assertEqual(str(e.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as e:
            s.size = -2
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_update(self):
        """test update"""
        r = Square(1, id=100)
        r.update(101)
        self.assertEqual(r.id, 101)
        r.update(102, 2)
        self.assertEqual((r.id, r.size), (102, 2))
        r.update(103, 3, 2)
        self.assertEqual((r.id, r.size, r.x), (103, 3, 2))
        r.update(104, 4, 3, 2)
        self.assertEqual((r.id, r.size, r.x, r.y), (104, 4, 3, 2))
        with self.assertRaises(TypeError):
            r.update(106, 6, 5, 4, 3, 2)
        r = Square(1, 1, id=100)
        r.update(1, 3, 4, id=101)
        self.assertEqual(r.id, 1)
        self.assertEqual((r.size, r.x, r.y), (3, 4, 0))
        r.update(id=102, size=10, x=0, y=0)
        self.assertEqual((r.id, r.size, r.x, r.y),
                         (102, 10, 0, 0))

    def test_to_dictionary(self):
        """test to_dictionary"""
        d = {'id': 0, 'size': 4, 'x': 1, 'y': 1}
        r = Square(4, 1, 1, 0)
        self.assertEqual(r.to_dictionary(), d)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
        with self.assertRaises(TypeError):
            r.to_dictionary(1.2)
        with self.assertRaises(TypeError):
            r.to_dictionary(float('inf'))
        with self.assertRaises(TypeError):
            r.to_dictionary(float('nan'))
        with self.assertRaises(TypeError):
            r.to_dictionary((1, 2))
        with self.assertRaises(TypeError):
            r.to_dictionary([1, 2])
        with self.assertRaises(TypeError):
            r.to_dictionary('abc')

    def test_str(self):
        """test string representation"""
        r = Square(4, 1, 3, 0)
        self.assertEqual(r.__str__(), '[Square] (0) 1/3 - 4')
        output = io.StringIO()
        sys.stdout = output
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '[Square] (0) 1/3 - 4\n')

    def test_save_to_file_fail(self):
        """test save_to_file fail cases"""
        mixed = [1, 2, 3, Square(2), Square(4)]
        with self.assertRaises(AttributeError):
            Square.save_to_file(mixed)

    def test_save_to_file_success(self):
        """test save_to_file success case"""
        sqs = [Square(4), Square(23, 4, 0)]
        Square.save_to_file(sqs)
        with open('Square.json', encoding='utf-8') as f:
            content = f.read()
        l = __import__('json').loads(content)
        self.assertEqual([e.to_dictionary() for e in sqs], l)
        os.remove('Square.json')
        Square.save_to_file(None)
        with open('Square.json', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, '[]')
        os.remove('Square.json')
        Square.save_to_file([])
        with open('Square.json', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, '[]')
        os.remove('Square.json')

    def test_create_fail(self):
        """ test create fail cases"""
        with self.assertRaises(TypeError):
            Square.create(invalidkey=5)
        with self.assertRaises(ValueError):
            Square.create(size=-2)
        with self.assertRaises(TypeError):
            Square.create(size='abc')
        with self.assertRaises(TypeError):
            Square.create(size=(1, 2, 3))
        with self.assertRaises(TypeError):
            Square.create('not a dictionary')
        with self.assertRaises(TypeError):
            Square.create([1, 2, 3])
        with self.assertRaises(TypeError):
            Square.create((1, 2, 3))
        with self.assertRaises(TypeError):
            Square.create(None)

    def test_create_success(self):
        """test create success cases"""
        d = {'id': 0, 'size': 4, 'x': 1, 'y': 1}
        r = Square(4, 1, 1, 0)
        self.assertEqual(Square.create(**d).to_dictionary(),
                         r.to_dictionary())

    def test_load_from_file(self):
        """test load_from_file"""
        sqs = [Square(2), Square(1, 3, 4, 0)]
        Square.save_to_file(sqs)
        sqs_dict = [e.to_dictionary() for e in sqs]
        l = Square.load_from_file()
        l = [e.to_dictionary() for e in l]
        self.assertEqual(sqs_dict, l)
        os.remove('Square.json')

if __name__ == "__main__":
    unittest.main()
