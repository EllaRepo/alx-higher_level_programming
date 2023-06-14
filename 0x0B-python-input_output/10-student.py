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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        dict_desc = self.__dict__.copy()
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return dict_desc
            n_list = {}
            for i in range(len(attrs)):
                for j in dict_desc:
                    if attrs[i] == j:
                        n_list[j] = dict_desc[j]
            return n_list
        return dict_desc
