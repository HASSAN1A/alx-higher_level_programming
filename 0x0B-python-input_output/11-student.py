#!/usr/bin/python3
"""class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    new_dict[item] = getattr(self, item)
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)