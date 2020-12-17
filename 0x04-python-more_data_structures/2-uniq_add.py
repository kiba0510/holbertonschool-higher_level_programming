#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    if my_list:
        for t in my_list:
            my_set.add(t)
    return sum(my_set)
