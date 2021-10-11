#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """that returns True if the object is exactly an instance
    of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
