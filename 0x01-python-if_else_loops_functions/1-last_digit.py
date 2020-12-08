#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last = number % 10
if (number < 0):
    number *= -1
    last = number % 10
    last *= -1
    number *= -1

if (last > 5):
    print("{} {} is {} and is greater than 5".format(str, number, last))

elif (last == 0):
    print("{} {} is {} and is 0".format(str, number, last))
elif (last < 6 and last != 0):
    print("{} {} is {} and is less than 6 and not 0".format(str, number, last))
