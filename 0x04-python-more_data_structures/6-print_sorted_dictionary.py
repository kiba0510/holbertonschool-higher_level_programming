#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = []
    if a_dictionary:
        for i, j in a_dictionary.items():
            key.append(i)

        key.sort()
        for i in key:
            print("{}: {}".format(i, a_dictionary[i]))
