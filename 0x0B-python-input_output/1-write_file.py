#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)
