#!/usr/bin/python3
"""Module defines a Base class.
"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"Writes the JSON string representation of list_objs to a file
        Args:
            list_objs: is a list of instances who inherits of Base
        """
        list_dic = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lsts = cls.to_json_string(list_dic)
        with open("{}.json".format(cls.__name__), 'w',) as f:
            f.write(lsts)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: is a string representing a list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            json_string = f.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
