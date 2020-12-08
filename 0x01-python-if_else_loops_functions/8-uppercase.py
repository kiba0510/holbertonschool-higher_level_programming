#!/usr/bin/python3
# Python function that prints a string
# in uppercase followed by a new line.


def uppercase(str):
    for u in str:
        print("{}".format(chr(ord(u) - 32)
                          if (ord(u) >= ord("a") and
                              ord(u) <= ord("z")) else u), end="")
    print('\n', end='')
