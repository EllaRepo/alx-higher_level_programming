#!/usr/bin/python3
"""Module for unittest for Square class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Unit test class for 'Square' module
    """
    def setUp(self):
        """Includes the function to be tested
        """
        Base._Base__nb_objects = 0

    def test_square(self):
        """Test new square instance with only size arg (default)
        """
        s = Square(4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_with_all_args(self):
        """Test new square with all args
        """
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_invalid_arg_amount(self):
        """Test square with invalid arg amount
        """
        with self.assertRaises(TypeError):
            s = Square()

    def test_square_cmp_ids(self):
        """Test square comparing ids
        """
        s1 = Square(10)
        s2 = Square(10)
        self.assertEqual(False, s1.id == s2.id)

    def test_square_cmp_instances(self):
        """Test new square with comparing instances
        """
        s1 = Square(10)
        s2 = Square(10)
        self.assertEqual(False, s1 is s2)

    def test_square_instance_type(self):
        """Test new square with comparing instances
        """
        s = Square(10)
        self.assertEqual(True, isinstance(s, Base))

    def test_square_instance_type_2(self):
        """Test new square with comparing instances
        """
        s = Square(10)
        self.assertEqual(True, isinstance(s, Rectangle))

    def test_square_invalid_arg_size(self):
        """Test new square with invalid arg size
        """
        with self.assertRaises(TypeError):
            s = Square(5, 2, 3, 4, 10)

    def test_square_invalid_size_type1(self):
        """Test new square with invalid size type
        """
        with self.assertRaises(TypeError):
            s = Square('1', 2, 3, 4)

    def test_square_invalid_size_type2(self):
        """Test new square with invalid size type
        """
        with self.assertRaises(ValueError):
            s = Square(-10)

    def test_square_invalid_x_type(self):
        """Test new square with invalid x type
        """
        with self.assertRaises(TypeError):
            s = Square(1, '2', 3, 4)

    def test_square_invalid_y_type(self):
        """Test new square with invalid y type
        """
        with self.assertRaises(TypeError):
            s = Square(1, 2, '3', 4)

    def test_square_invalid_size_value(self):
        """Test new square with invalid size value
        """
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_square_invalid_x_value(self):
        """Test new square with invalid x value
        """
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_square_invalid_y_value(self):
        """Test new square with invalid y value
        """
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_access_private_attribute_width(self):
        """Test accessing private class attribute
        """
        s = Square(1, 2)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_private_attribute_height(self):
        """Test accessing private class attribute
        """
        s = Square(1, 2)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_private_attribute_x(self):
        """Test accessing private class attribute
        """
        s = Square(1, 2)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_private_attribute_y(self):
        """Test accessing private class attribute
        """
        s = Square(1, 2)
        with self.assertRaises(AttributeError):
            s.__y

    def test_square_area_1(self):
        """Test square area
        """
        s = Square(8)
        self.assertEqual(s.area(), 64)

    def test_square_area_2(self):
        """Test square area
        """
        s = Square(12)
        self.assertEqual(s.area(), 144)
        s.size = 10
        self.assertEqual(s.area(), 100)

    def test_square_area_3(self):
        """Test Square area
        """
        s1 = Square(12)
        s2 = Square(4)
        self.assertEqual(s1.area(), 144)
        self.assertEqual(s2.area(), 16)

    def test_square_display_1(self):
        """Test Square display
        """
        s = Square(2)
        dis = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_square_display_2(self):
        """Test square display
        """
        s = Square(1)
        dis = "#\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_square_display_3(self):
        """Test square display
        """
        s = Square(5)
        dis = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), dis)
        s.size = 2
        dis = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_square_str_1(self):
        """Test square __str__ return value
        """
        s = Square(2)
        ret = "[Square] (1) 0/0 - 2"
        self.assertEqual(s.__str__(), ret)

    def test_square_str_2(self):
        """Test square __str__
        """
        s1 = Square(2)
        s2 = Square(8, 14, 3, 5)
        ret1 = "[Square] (1) 0/0 - 2"
        ret2 = "[Square] (5) 14/3 - 8"
        self.assertEqual(s1.__str__(), ret1)
        self.assertEqual(s2.__str__(), ret2)

    def test_square_str_3(self):
        """Test square __str__ return value
        """
        s = Square(8, 3, 5, 7)
        ret = "[Square] (7) 3/5 - 8"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s, end='')
            self.assertEqual(std_out.getvalue(), ret)
        s.id = 5
        s.size = 10
        s.x = 9
        s.y = 2
        ret = "[Square] (5) 9/2 - 10"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s, end='')
            self.assertEqual(std_out.getvalue(), ret)

    def test_square_str_4(self):
        """Test square __str__ return value
        """
        s = Square(1)
        ret = "[Square] (1) 0/0 - 1"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s, end='')
            self.assertEqual(std_out.getvalue(), ret)
        s2 = Square(8, 3, 4)
        ret = "[Square] (2) 3/4 - 8"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s2, end='')
            self.assertEqual(std_out.getvalue(), ret)
        s3 = Square(19, 4, 8, 7)
        ret = "[Square] (7) 4/8 - 19"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s3, end='')
            self.assertEqual(std_out.getvalue(), ret)

    def test_square_display_6(self):
        """Test string printed by display method
        """
        s = Square(2)
        dis = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), dis)

    def test_square_display_7(self):
        """Test string printed by display method
        """
        s = Square(5, 1, 1)
        dis = "\n #####\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_square_display_8(self):
        """Test string printed by display method
        """
        s = Square(5, 2)
        dis = "  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_square_display_9(self):
        """Test string printed by display method
        """
        s = Square(5, 0, 2)
        dis = "\n\n#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_square_display_10(self):
        """Test string printed by display method
        """
        s = Square(3)
        dis = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

        s.x = 3
        dis = "   ###\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

        s.y = 4
        dis = "\n\n\n\n   ###\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), dis)

    def test_square_update_1(self):
        """Test attributes updated by update method
        """
        s = Square(5, 4, 3, 4)
        s.update(45)
        self.assertEqual(s.id, 45)

    def test_square_update_2(self):
        """Test attributes updated by update method
        """
        s = Square(5, 4, 3, 4)
        s.update(45, 78)
        self.assertEqual(s.id, 45)
        self.assertEqual(s.size, 78)
        self.assertEqual(s.width, 78)
        self.assertEqual(s.height, 78)

    def test_Square_update_3(self):
        """Test attributes updated by update method
        """
        s = Square(5, 4, 3, 4)
        s.update(45, 78, 34)
        self.assertEqual(s.id, 45)
        self.assertEqual(s.size, 78)
        self.assertEqual(s.width, 78)
        self.assertEqual(s.height, 78)
        self.assertEqual(s.x, 34)

    def test_square_update_4(self):
        """Test attributes updated by update method
        """
        s = Square(5, 4, 3, 4)
        s.update(45, 78, 34, 8)
        self.assertEqual(s.id, 45)
        self.assertEqual(s.size, 78)
        self.assertEqual(s.width, 78)
        self.assertEqual(s.height, 78)
        self.assertEqual(s.x, 34)
        self.assertEqual(s.y, 8)

    def test_square_update_5(self):
        """Test attributes updated by update method
        """
        s = Square(10)
        ret = "[Square] (1) 0/0 - 10"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s, end='')
            self.assertEqual(str_out.getvalue(), ret)

        dic = {'size': 5, 'y': 8}
        s.update(**dic)
        ret = "[Square] (1) 0/8 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), ret)

        dic = {'id': 45, 'x': 78}
        s.update(**dic)
        ret = "[Square] (45) 78/8 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), ret)

    def test_square_dictionary(self):
        """ Test dictionary returned
        """
        s = Square(14, 16, 19)
        ret = "[Square] (1) 16/19 - 14"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s, end='')
            self.assertEqual(str_out.getvalue(), ret)

        self.assertEqual(s.size, 14)
        self.assertEqual(s.width, 14)
        self.assertEqual(s.height, 14)
        self.assertEqual(s.x, 16)
        self.assertEqual(s.y, 19)
        self.assertEqual(s.id, 1)

        ret = "<class 'dict'>"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s.to_dictionary()), end='')
            self.assertEqual(str_out.getvalue(), ret)

    def test_square_dictionary_2(self):
        """ Test dictionary returned
        """
        s1 = Square(6, 14, 8, 10)
        ret = "[Square] (10) 14/8 - 6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), ret)

        s2 = Square(26)
        ret = "[Square] (1) 0/0 - 26"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2, end='')
            self.assertEqual(str_out.getvalue(), ret)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        ret = "<class 'dict'>"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary), end='')
            self.assertEqual(str_out.getvalue(), ret)

    def test_square_dict_to_json(self):
        """ Test Dictionary to JSON string
        """
        s = Square(2)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        ret = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), ret.replace("'", "\""))

    def test_square_json_file(self):
        """ Test Dictionary to JSON string
        """
        s1 = Square(5)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([s1])
        res = "[{}]".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with open("Square.json", "r") as file:
            res2 = file.read()

        self.assertEqual(res, res2)

    def test_square_create(self):
        """ Test create method
        """
        dic = {'id': 7}
        s = Square.create(**dic)
        self.assertEqual(s.id, 7)

    def test_square_create_2(self):
        """ Test create method
        """
        dic = {'id': 7, 'size': 10}
        s = Square.create(**dic)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 10)

    def test_square_create_3(self):
        """ Test create method
        """
        dic = {'id': 7, 'size': 10, 'x': 4}
        s = Square.create(**dic)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)

    def test_square_create_4(self):
        """ Test create method
        """
        dic = {'id': 7, 'size': 10, 'x': 4, 'y': 6}
        s = Square.create(**dic)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_square_load_from_file_2(self):
        """ Test load JSON file
        """
        s1 = Square(15)
        s2 = Square(1, 2, 3)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

    def test_square_save_to_file_1(self):
        """Test save to JSON file
        """
        Square.save_to_file(None)
        load_file = Square.load_from_file()
        self.assertEqual(load_file, [])

    def test_square_save_to_file_2(self):
        """Test save to JSON file
        """
        Square.save_to_file([Square(2)])
        Square.save_to_file([])
        load_file = Square.load_from_file()
        self.assertEqual(load_file, [])
