#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = []
    for key, val in a_dictionary.items():
        if (val == value):
            k.append(key)
    for x in k:
        del a_dictionary[x]
    return (a_dictionary)
