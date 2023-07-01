#!/usr/bin/python3
"""Class Base"""
import json


class Base():
    """Class Base
    Args:
        id
    Method:
        __init__(self, id)
        to_json_string(list_dictionaries)
        from_json_string(json_string)
        create(cls, **dictionary)
        load_from_file(cls)
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
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if dictionary:
            new_obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jfile:
                list_dcts = Base.from_json_string(jfile.read())
                return [cls.create(**dct) for dct in list_dcts]
        except IOError:
            return []
