#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle():
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """initialize Rectangle with args width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get - set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get - set height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the Rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))