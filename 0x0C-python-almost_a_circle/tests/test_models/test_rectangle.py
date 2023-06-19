#!/usr/bin/python3
"""Module for unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit test class for 'rectangle' module
    """
    def setUp(self):
        """Includes the function to be tested
        """
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """Test new rectangle (default)
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_with_all_args(self):
        """Test new rectangle with all args
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_invalid_arg_amount(self):
        """Test rectangle with invalid arg amount
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_rectangle_cmp_ids(self):
        """Test rectangles comparing ids
        """
        r1 = Rectangle(10, 10)
        r2 = Rectangle(10, 10)
        self.assertEqual(False, r1.id == r2.id)

    def test_rectangle_cmp_instances(self):
        """Test new rectangle with comparing instances
        """
        r1 = Rectangle(10, 10)
        r2 = Rectangle(10, 10)
        self.assertEqual(False, r1 is r2)

    def test_rectangle_instance_type(self):
        """Test new rectangle with comparing instances
        """
        r1 = Rectangle(10, 10)
        self.assertEqual(True, isinstance(r1, Base))

    def test_rectangle_invalid_width_type(self):
        """Test new rectangle with invalid width type
        """
        with self.assertRaises(TypeError):
            r = Rectangle('1', 2, 3, 4)

    def test_rectangle_invalid_height_type(self):
        """Test new rectangle with invalid height type
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, '2', 3, 4)

    def test_rectangle_invalid_x_type(self):
        """Test new rectangle with invalid x type
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, '3', 4)

    def test_rectangle_invalid_y_type(self):
        """Test new rectangle with invalid y type
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, '4')

    def test_rectangle_invalid_width_value(self):
        """Test new rectangle with invalid width value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_rectangle_invalid_width_value1(self):
        """Test new rectangle with invalid width value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_rectangle_invalid_height_value(self):
        """Test new rectangle with invalid height value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_rectangle_invalid_height_value1(self):
        """Test new rectangle with invalid height value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = -10

    def test_rectangle_invalid_x_value(self):
        """Test new rectangle with invalid x value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.x = -10

    def test_rectangle_invalid_y_value(self):
        """Test new rectangle with invalid y value
        """
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.y = -10

    def test_access_private_attribute_width(self):
        """Test accessing private class attribute
        """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_access_private_attribute_height(self):
        """Test accessing private class attribute
        """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__height

    def test_access_private_attribute_x(self):
        """Test accessing private class attribute
        """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__x

    def test_access_private_attribute_y(self):
        """Test accessing private class attribute
        """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__y

    def test_rectangle_area_1(self):
        """Test rectangle area
        """
        r = Rectangle(24, 2)
        self.assertEqual(r.area(), 48)

    def test_rectangle_area_2(self):
        """Test rectangle area
        """
        r = Rectangle(24, 2)
        self.assertEqual(r.area(), 48)
        r.width = 10
        self.assertEqual(r.area(), 20)

    def test_rectangle_area_3(self):
        """Test rectangle area
        """
        r = Rectangle(24, 2)
        self.assertEqual(r.area(), 48)
        r.height = 10
        self.assertEqual(r.area(), 240)

    def test_rectangle_area_4(self):
        """Test rectangle area
        """
        r = Rectangle(24, 2)
        self.assertEqual(r.area(), 48)
        r.width = 2
        r.height = 4
        self.assertEqual(r.area(), 8)

    def test_rectangle_area_54(self):
        """Test rectangle area
        """
        r1 = Rectangle(12, 2)
        r2 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 24)
        self.assertEqual(r2.area(), 20)

    def test_rectangle_display_1(self):
        """Test rectangle display
        """
        r = Rectangle(2, 4)
        dis = "##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_display_2(self):
        """Test rectangle display
        """
        r = Rectangle(1, 1)
        dis = "#\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_display_3(self):
        """Test rectangle display
        """
        r = Rectangle(3, 1)
        dis = "###\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_display_4(self):
        """Test rectangle display
        """
        r = Rectangle(1, 3)
        dis = "#\n#\n#\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_display_5(self):
        """Test rectangle display
        """
        r = Rectangle(5, 3)
        dis = "#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)
        r.height = 5
        dis = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)
        r.width = 2
        dis = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_str_1(self):
        """Test rectangle __str__ return value
        """
        r = Rectangle(2, 4)
        ret = "[Rectangle] (1) 0/0 - 2/4"
        self.assertEqual(r.__str__(), ret)

    def test_rectangle_str_2(self):
        """Test rectangle __str__
        """
        r1 = Rectangle(2, 4)
        r2 = Rectangle(8, 14, 3, 5, 6)
        ret1 = "[Rectangle] (1) 0/0 - 2/4"
        ret2 = "[Rectangle] (6) 3/5 - 8/14"
        self.assertEqual(r1.__str__(), ret1)
        self.assertEqual(r2.__str__(), ret2)

    def test_rectangle_str_3(self):
        """Test rectangle __str__ return value
        """
        r = Rectangle(1, 3, 5, 7)
        ret = "[Rectangle] (1) 5/7 - 1/3"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r, end='')
            self.assertEqual(std_out.getvalue(), ret)

    def test_rectangle_str_4(self):
        """Test rectangle __str__ return value
        """
        r = Rectangle(1, 3, 5, 7, 56)
        ret = "[Rectangle] (56) 5/7 - 1/3"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r, end='')
            self.assertEqual(std_out.getvalue(), ret)
        r.width = 10
        r.height = 25
        r.x = 9
        r.y = 2
        ret = "[Rectangle] (56) 9/2 - 10/25"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r, end='')
            self.assertEqual(std_out.getvalue(), ret)

    def test_rectangle_str_5(self):
        """Test rectangle __str__ return value
        """
        r = Rectangle(1, 3)
        ret = "[Rectangle] (1) 0/0 - 1/3"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r, end='')
            self.assertEqual(std_out.getvalue(), ret)
        r2 = Rectangle(1, 3, 4, 8)
        ret = "[Rectangle] (2) 4/8 - 1/3"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r2, end='')
            self.assertEqual(std_out.getvalue(), ret)
        r3 = Rectangle(1, 3, 4, 8, 7)
        ret = "[Rectangle] (7) 4/8 - 1/3"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r3, end='')
            self.assertEqual(std_out.getvalue(), ret)

    def test_rectangle_display_6(self):
        """Test string printed by display method
        """
        r = Rectangle(2, 4)
        dis = "##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_rectangle_display_7(self):
        """Test string printed by display method
        """
        r = Rectangle(5, 4, 1, 1)
        dis = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_rectangle_display_8(self):
        """Test string printed by display method
        """
        r = Rectangle(5, 4, 2)
        dis = "  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_rectangle_display_9(self):
        """Test string printed by display method
        """
        r = Rectangle(5, 4, 0, 2)
        dis = "\n\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_rectangle_display_10(self):
        """Test string printed by display method
        """
        r = Rectangle(3, 2)
        dis = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

        r.x = 3
        dis = "   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

        r.y = 4
        dis = "\n\n\n\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_rectangle_update_1(self):
        """Test attributes updated by update method
        """
        r = Rectangle(5, 4, 3, 4)
        r.update(45)
        self.assertEqual(r.id, 45)

    def test_rectangle_update_2(self):
        """Test attributes updated by update method
        """
        r = Rectangle(5, 4, 3, 4)
        r.update(45, 78)
        self.assertEqual(r.id, 45)
        self.assertEqual(r.width, 78)

    def test_rectangle_update_3(self):
        """Test attributes updated by update method
        """
        r = Rectangle(5, 4, 3, 4)
        r.update(45, 78, 34)
        self.assertEqual(r.id, 45)
        self.assertEqual(r.width, 78)
        self.assertEqual(r.height, 34)

    def test_rectangle_update_4(self):
        """Test attributes updated by update method
        """
        r = Rectangle(5, 4, 3, 4)
        r.update(45, 78, 34, 8)
        self.assertEqual(r.id, 45)
        self.assertEqual(r.width, 78)
        self.assertEqual(r.height, 34)
        self.assertEqual(r.x, 8)

    def test_rectangle_update_5(self):
        """Test attributes updated by update method
        """
        r = Rectangle(5, 4, 3, 4)
        r.update(45, 78, 34, 8, 9)
        self.assertEqual(r.id, 45)
        self.assertEqual(r.width, 78)
        self.assertEqual(r.height, 34)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def test_rectangle_dictionary(self):
        """ Test dictionary returned """
        r = Rectangle(1, 2, 3, 4, 1)
        ret = "[Rectangle] (1) 3/4 - 1/2"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r, end='')
            self.assertEqual(str_out.getvalue(), ret)

        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)

        ret = "<class 'dict'>"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r.to_dictionary()), end='')
            self.assertEqual(str_out.getvalue(), ret)

    def test_rectangle_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        ret = "[Rectangle] (1) 2/2 - 2/2"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1, end='')
            self.assertEqual(str_out.getvalue(), ret)

        r2 = Rectangle(5, 7)
        ret = "[Rectangle] (2) 0/0 - 5/7"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2, end='')
            self.assertEqual(str_out.getvalue(), ret)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        ret = "<class 'dict'>"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary), end='')
            self.assertEqual(str_out.getvalue(), ret)

    def test_rectangle_dict_to_json(self):
        """Test Dictionary to JSON string
        """
        r = Rectangle(2, 2)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_rectangle_create(self):
        """Test create method
        """
        dic = {'id': 7}
        r = Rectangle.create(**dic)
        self.assertEqual(r.id, 7)

    def test_rectangle_create_2(self):
        """Test create method
        """
        dic = {'id': 7, 'width': 15}
        r = Rectangle.create(**dic)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 15)

    def test_rectangle_create_3(self):
        """Test create method
        """
        dic = {'id': 7, 'width': 15, 'height': 10}
        r = Rectangle.create(**dic)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 10)

    def test_rectangle_create_4(self):
        """Test create method
        """
        dic = {'id': 7, 'width': 15, 'height': 10, 'x': 3}
        r = Rectangle.create(**dic)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 3)

    def test_rectangle_create_5(self):
        """Test create method
        """
        dic = {'id': 7, 'width': 15, 'height': 10, 'x': 3, 'y': 8}
        r = Rectangle.create(**dic)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 8)

    def test_rectangle_load_from_file(self):
        """Test load JSON file
        """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_rectangle_load_from_file_2(self):
        """Test load JSON file
        """
        r1 = Rectangle(8, 7)
        r2 = Rectangle(8, 2, 5, 5)

        l_input = [r1, r2]
        Rectangle.save_to_file(l_input)
        l_output = Rectangle.load_from_file()

        for i in range(len(l_input)):
            self.assertEqual(l_input[i].__str__(), l_output[i].__str__())


if __name__ == '__main__':
    unittest.main()
