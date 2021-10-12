#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename) as a_file:
        return json.load(a_file)

