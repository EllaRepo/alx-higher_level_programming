#!/usr/bin/python3
""" This module defines a LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    """Class LockedClass with no class or object attribute.

    """
    __slots__ = ['first_name']

    def __init__(self) -> None:
        """Initializes class instance
        """
        pass
