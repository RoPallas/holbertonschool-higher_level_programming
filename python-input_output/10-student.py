#!/usr/bin/python3
"""class Student"""


class Student:
    """A student"""

    def __init__(self, first_name, last_name, age):
        """Initialize an object Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dict_attrs = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                dict_attrs[attr] = self.__dict__[attr]
        return dict_attrs
