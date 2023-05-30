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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (isinstance(value[0], int) or isinstance(value[1], int)):
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
        if not self.__size:
            print()
        else:
            if not self.__position:
                pass
            else:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                if self.__position:
                    for k in range(self.__position[0]):
                        print("_", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
