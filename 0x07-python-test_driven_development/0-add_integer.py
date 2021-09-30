#!/usr/bin/python3
"""Module to find
the sum of two
integers or
Floats
"""


def add_integer(a, b=98):
    """Function to find and return sum of two integers or floats
    Is first variable int or float?
    Is second variable int or float?"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
