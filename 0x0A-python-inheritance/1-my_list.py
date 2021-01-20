#!/usr/bin/python3
"""
Class method MyList with attributes of list
"""


class MyList(list):
    """
    class method that inherits a list
    """
    def print_sorted(self):
        print(sorted(self))
