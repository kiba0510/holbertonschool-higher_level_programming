#!/usr/bin/python3
"""
Defining load_from_json_file
"""
import json


def load_from_json_file(filename):
    '''
    Function that creates an Object from a JSON file
    '''
    with open(filename, encoding="UTF-8") as fl:
        return json.load(fl)
