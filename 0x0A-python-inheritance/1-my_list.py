#!/usr/bin/python3
"""
Defining is_same_class function
"""

def is_same_class(obj, a_class):
    """
    Fuction that checks if obj have same class
    """
    if type(obj) is a_class:
        return True
    return False
