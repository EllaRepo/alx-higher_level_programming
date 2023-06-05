#!/usr/bin/python3
""" This module defines a Rectangle class.
"""


class Rectangle:
    """Empty class Rectangle that defines a rectangle.

    """
    number_of_instances = 0
    print_symbol = "#"

    def __str__(self):
        """Prints in stdout the Rectangle with the character #
        """
        rect_str = ""
        if self.width == 0 or self.height == 0:
            return rect_str
        else:
            for i in range(self.height):
                rect_str += (str(self.print_symbol) * self.width) + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle to be able to
           recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Return a string representation of the rectangle to be able to
           recreate a new instance by using eval()
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __init__(self, width=0, height=0):
        """Initialize method that stores value for private attribute width
            and height.

        Args:
            width (int): width of the square.
            height (int): height of the square.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set private instance attribute width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set private instance attribute height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
