#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    d = -(((number) * (-1)) % 10)
else:
    d = number % 10

if d > 5:
    print(f"Last digit of {number} is {d} and is greater than 5")
elif d == 0:
    print(f"Last digit of {number} is {d} and is 0")
elif d < 6 and d != 0:
    print(f"Last digit of {number} is {d} and is less than 6 and not 0")
