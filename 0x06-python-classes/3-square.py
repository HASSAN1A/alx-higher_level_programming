#!/usr/bin/python3
"""define a class Square"""


class Square:
    """private size attribute for Square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """returns the current square area"""
    def area(self):
        return self.__size ** 2
