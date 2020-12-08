#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater_5 = "and is greater that 5"
zero = "and is 0"
less_6 = "and is less that 6 and not 0"
print("Last digit of", end=" ")
if (number % 10 > 5):
    print("{} is {} {}".format(number, number % 10, greater_5))
elif (number % 10 == 0):
    print("{} is {} {}".format(number, number % 10, zero))
elif (number < 0):
    print("{} is -{} {}".format(number, number * -1, less_6))
else:
    print("{} is {} {}".format(number, number % 10, less_6))
