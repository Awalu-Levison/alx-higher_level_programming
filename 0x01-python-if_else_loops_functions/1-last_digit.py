#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
if number < 0:
    last_num = -(last_num)
mystring = "Last digit of {} is {}".format(number, last_num)
if number > 5:
    print(f"{mystring} and is greater than 5")
elif number == 0:
    print(f"{mystring} and is 0")
elif number < 6:
    print(f"{mystring} and is less than 6 and not 0")
