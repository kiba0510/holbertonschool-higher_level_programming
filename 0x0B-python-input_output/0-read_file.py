#!/usr/bin/python3
"""
Function to read a file
"""


def read_file(filename=""):
    '''
    read_file Function
    '''
    with open(filename, encoding="UTF-8") as readr:
        print(readr.read(), end="")
