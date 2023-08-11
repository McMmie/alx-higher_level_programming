#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10
if rem > 5:
    print(f"Last digit of {number} is {rem:d} and is greater than 5")
elif rem == 0:
    print(f"Last digit of {number} is {rem:d} and is 0")
elif (rem < 6) | (rem != 0):
    print(f"Last digit of {number} is {rem:d} and is less than 6 and is not 0")
