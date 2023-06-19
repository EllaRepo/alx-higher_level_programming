#!/usr/bin/python3
""" This module defines a Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor

        Args:
            size: size of the square.
            x: x
            y: y
            id: id
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns instance information
        """
        info = "[Square] ({}) {}/{} - {}"
        return info.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Retrieve private instance attribute width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set private instance attribute width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """" Assigns an argument to each attribute
        Args:
            *args: variable args
            **kwargs: variable key-value args
        """
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attrs))):
                if attrs[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        attrs = ['id', 'size', 'x', 'y']
        dic = {}

        for key in attrs:
            if key == 'size':
                dic[key] = getattr(self, 'width')
            else:
                dic[key] = getattr(self, key)
        return dic
