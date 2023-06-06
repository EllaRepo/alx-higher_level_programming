#!/usr/bin/python3
""" This module defines a LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """Initializes the class
        """
        pass
