#!/usr/bin/python3
# Python function that prints a string
# in uppercase followed by a new line.


def uppercase(str):
    for up in str:
        print("{}".format(chr(ord(up) - 32)
                          if (ord(up) >= ord("a") and
                              ord(up) <= ord("z")) else up), end="")
    print()
