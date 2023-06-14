#!/usr/bin/python3
""" This module defines a Student class.
"""


class Student:
    """class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize method.
        Args:
            first_name: first name
            last_name: last name
            age: age of a studen
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__.copy()
