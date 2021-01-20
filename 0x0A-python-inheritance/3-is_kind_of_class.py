#!/usr/bin/python3
"""
Defining is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks the type of class and inherited class
    """
    if isinstance(obj, a_class):
        return True
    return False
