#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
mess = f"Last digit of {number} is {last}"
if number < 0:
    mess = f"Last digit of {number} is -{last}"
if last > 5:
    print(mess + " and is greater than 5")
elif last == 0:
    print(mess + " and is 0")
elif last < 6 and last != 0:
    print(mess + " and is less than 6 and not 0")
