#!/usr/bin/python3
""" This module defines a LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    def __setattr__(self, key, value):
        if hasattr(self, key) or key != 'first_name':
            c_name = self.__class__.__name__
            msg = "object has no attribute"
            raise AttributeError("\'{}\' {} \'{}\'".format(c_name, msg, key))
        super().__setattr__(key, value)
