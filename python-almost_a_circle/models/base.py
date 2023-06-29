#!/usr/bin/python3
"""Class Base"""
import json


class Base():
    """Class Base
    Args:
        id
    Method:
        __init__(self, id)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization Class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"""

        if list_objs is None:
            data = "[]"
        else:
            data = [obj.to_dictionaty() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            jsonfile.write(Base.to_json_string(data))
