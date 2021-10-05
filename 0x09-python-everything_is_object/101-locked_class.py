#!/usr/bin/python3
"""module that defines a locked class."""


class LockedClass:
    """allows ONLY first_name attribute"""

    __slots__ = ["first_name"]