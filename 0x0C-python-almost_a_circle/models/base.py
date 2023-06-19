#!/usr/bin/python3
"""Module defines a Base class.
"""


class Base:
    """Class Base - “base” of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance.
        Args:
            id: integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
