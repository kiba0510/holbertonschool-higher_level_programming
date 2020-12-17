#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for x, t in enumerate(new_list):
        if (t == search):
            new_list[x] = replace
    return (new_list)
