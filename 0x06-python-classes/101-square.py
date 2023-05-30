#!/usr/bin/python3
""" This module defines a Square class.
"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize method that stores value for private attribute size.

        Args:
            size (int): Size of the square.
            position (int tuple): position of the square
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Prints in stdout the square with the character #
        """
        square_str = ""
        if not self.size:
            square_str += "\n"
        else:
            for i in range(self.position[1]):
                square_str += "\n"
            for i in range(self.size):
                for k in range(self.position[0]):
                    square_str += " "
                for j in range(self.size):
                    square_str += "#"
                square_str += "\n"
        return square_str

    @property
    def size(self):
        """Retrieve private instance attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set private instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(value)

    @property
    def position(self):
        """Retrieve private instance attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set private instance attribute position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the current square area.
        """
        return self.__size**2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if not self.size:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
