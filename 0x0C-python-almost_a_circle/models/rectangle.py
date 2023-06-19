#!/usr/bin/python3
""" This module defines a Rectangle class.
"""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x: x
            y: y
            id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Returns instance information
        """
        info = "[Rectangle] ({}) {}/{} - {}/{}"
        return info.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Retrieve private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set private instance attribute width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieve private instance attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set private instance attribute x
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieve private instance attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set private instance attribute y
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Instance method that returns the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """Prints in stdout the Rectangle with the character #
        """
        for i in range(self.y):
                print()
        for i in range(self.height):
            for k in range(self.x):
                    print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """" Assigns an argument to each attribute

        Args:
            *args: variable args
        """
        if args and len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)