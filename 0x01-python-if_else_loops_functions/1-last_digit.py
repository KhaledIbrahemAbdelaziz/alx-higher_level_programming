#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
digit = abs(number) % 10
if number < 0:
    digit = -1 * digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 0:
    print("greater than 5")
elif digit < 0:
    print("less than 6 and not 0")
else:
    print("0")
