#!/usr/bin/python3
"""define a class Square"""


class Square:
    """private size attribute for Square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """returns the current square area"""
    def area(self):
        return self.__size ** 2
