#!/usr/bin/python3
"""test class Rectangle"""
import unittest
import io
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test Rectangle class"""

    def test_init_error_width_height(self):
        """test constructor fail cases"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle('a', 2)
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 2)
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 2)
        with self.assertRaises(TypeError):
            Rectangle({'1': 'one'}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1.2, 2)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2)
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 2)
        with self.assertRaises(ValueError):
            Rectangle(-2, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 'a')
        with self.assertRaises(TypeError):
            Rectangle(1, [1, 2])
        with self.assertRaises(TypeError):
            Rectangle(1, [1, 2])
        with self.assertRaises(TypeError):
            Rectangle(1, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(1, {'1': 'one'})
        with self.assertRaises(TypeError):
            Rectangle(1, 1.2)
        with self.assertRaises(TypeError):
            Rectangle(1, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(1, float('nan'))
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_init_error_x_y(self):
        """test constructor error cases"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'x', 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [1, 2], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (1, 2), 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {'1': 'one'}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, True, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1.2, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -2, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2, 'y')
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 2, -2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_init_success(self):
        """test init valid cases"""
        rec = Rectangle(2, 4)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y), (2, 4, 0, 0))
        rec = Rectangle(2, 4, 1)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y), (2, 4, 1, 0))
        rec = Rectangle(2, 4, 1, 3)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y), (2, 4, 1, 3))
        rec = Rectangle(2, 4, 1, 3, 98)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y), (2, 4, 1, 3))

    def test_area(self):
        """test area"""
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)
        with self.assertRaises(TypeError):
            r.area(1)
        with self.assertRaises(TypeError):
            r.area([1, 2])
        with self.assertRaises(TypeError):
            r.area((1, 2))
        with self.assertRaises(TypeError):
            r.area({'1': 'one'})
        with self.assertRaises(TypeError):
            r.area(False)
        with self.assertRaises(TypeError):
            r.area(1.2)
        with self.assertRaises(TypeError):
            r.area(float('inf'))
        with self.assertRaises(TypeError):
            r.area(float('nan'))

    def test_display(self):
        """test display"""
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 4).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '##\n##\n##\n##\n')
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 4, 1, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '\n\n ##\n ##\n ##\n ##\n')
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.display(1)
        with self.assertRaises(TypeError):
            r.display([1, 2])
        with self.assertRaises(TypeError):
            r.display((1, 2))
        with self.assertRaises(TypeError):
            r.display({'1': 'one'})
        with self.assertRaises(TypeError):
            r.display(False)
        with self.assertRaises(TypeError):
            r.display(1.2)
        with self.assertRaises(TypeError):
            r.display(float('inf'))
        with self.assertRaises(TypeError):
            r.display(float('nan'))

    def test_update(self):
        """test update"""
        r = Rectangle(1, 1, id=100)
        r.update(101)
        self.assertEqual(r.id, 101)
        r.update(102, 2)
        self.assertEqual((r.id, r.width), (102, 2))
        r.update(103, 3, 2)
        self.assertEqual((r.id, r.width, r.height), (103, 3, 2))
        r.update(104, 4, 3, 2)
        self.assertEqual((r.id, r.width, r.height, r.x), (104, 4, 3, 2))
        r.update(105, 5, 4, 3, 2)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (105, 5, 4, 3, 2))
        with self.assertRaises(TypeError):
            r.update(106, 6, 5, 4, 3, 2)
        r = Rectangle(1, 1, id=100)
        r.update(1, 2, 3, 4, id=101)
        self.assertEqual(r.id, 1)
        self.assertEqual((r.width, r.height, r.x, r.y), (2, 3, 4, 0))
        r.update(id=102, width=1, height=1, x=0, y=0)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (102, 1, 1, 0, 0))

    def test_to_dictionary(self):
        """test to_dictionary"""
        d = {'id': 0, 'width': 2, 'height': 4, 'x': 1, 'y': 1}
        r = Rectangle(2, 4, 1, 1, 0)
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
        """test __str__"""
        r = Rectangle(2, 4, 1, 3, 0)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 1/3 - 2/4')
        output = io.StringIO()
        sys.stdout = output
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '[Rectangle] (0) 1/3 - 2/4\n')

    def test_save_to_file_fail(self):
        """test save_to_file fail cases"""
        mixed = [1, 2, 3, Rectangle(2, 4), Rectangle(1, 2, 3, 4, 0)]
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(mixed)

    def test_save_to_file_success(self):
        """test save_to_file success case"""
        recs = [Rectangle(2, 4), Rectangle(1, 2, 3, 4, 0)]
        Rectangle.save_to_file(recs)
        with open('Rectangle.json', encoding='utf-8') as f:
            content = f.read()
        l = __import__('json').loads(content)
        self.assertEqual([e.to_dictionary() for e in recs], l)
        os.remove('Rectangle.json')

    def test_create_fail(self):
        """ test create fail cases"""
        with self.assertRaises(TypeError):
            Rectangle.create(invalidkey=5)
        with self.assertRaises(ValueError):
            Rectangle.create(width=-2)
        with self.assertRaises(TypeError):
            Rectangle.create(width='abc')
        with self.assertRaises(TypeError):
            Rectangle.create(width=(1, 2, 3))
        with self.assertRaises(TypeError):
            Rectangle.create('not a dictionary')
        with self.assertRaises(TypeError):
            Rectangle.create([1, 2, 3])
        with self.assertRaises(TypeError):
            Rectangle.create((1, 2, 3))
        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_create_success(self):
        """test create success cases"""
        d = {'id': 0, 'width': 2, 'height': 4, 'x': 1, 'y': 1}
        r = Rectangle(2, 4, 1, 1, 0)
        self.assertEqual(Rectangle.create(**d).to_dictionary(),
                         r.to_dictionary())

    def test_load_from_file(self):
        """test load_from_file"""
        recs = [Rectangle(2, 4), Rectangle(1, 2, 3, 4, 0)]
        Rectangle.save_to_file(recs)
        recs_dict = [e.to_dictionary() for e in recs]
        l = Rectangle.load_from_file()
        l = [e.to_dictionary() for e in l]
        self.assertEqual(recs_dict, l)
        os.remove('Rectangle.json')

if __name__ == "__main__":
    unittest.main()
