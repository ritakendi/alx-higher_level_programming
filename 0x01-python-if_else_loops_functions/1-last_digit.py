#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 6:
   last_digit = number % 10
else:
   last_digit = number % -10
if last_digit < 6:
   print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and no 0")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit:d} and is 0")
else:
    print(f"Last digit {number} is {last_digit:d} and is greater than 5")
