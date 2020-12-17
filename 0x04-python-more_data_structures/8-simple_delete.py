#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        try:
            a_dictionary.pop(key)
        except KeyError:
            pass
    return (a_dictionary)
