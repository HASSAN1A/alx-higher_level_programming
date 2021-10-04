#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """private width and height attributes for Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize Rectangle with args width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """get/set height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is int:
            if val >= 0:
                self.__height = val
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """get/set width"""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is int:
            if val >= 0:
                self.__width = val
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")