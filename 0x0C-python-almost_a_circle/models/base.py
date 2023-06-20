#!/usr/bin/python3
"""Module defines a Base class.
"""
import csv
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
        if list_objs is None or len(list_objs) == 0:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that saves a CSV file
        Args:
            list_objs: list of objects
        """
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            l_dic = ['0', '0', '0', '0', '0']
            l_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            l_dic = ['0', '0', '0', '0']
            l_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs or len(list_objs) == 0:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(l_keys)):
                    l_dic[kv] = obj.to_dictionary()[l_keys[kv]]
                matrix.append(l_dic[:])

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file
        Args:
            list_objs: list of objects
        """
        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            l_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            l_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for elem in csv_list:
            dict_csv = {}
            for kv in enumerate(elem):
                dict_csv[l_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
