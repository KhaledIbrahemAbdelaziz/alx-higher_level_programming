#!/usr/bin/python3
for number in range(0, 10):
    for number1 in range(number + 1, 10):
        if number == 8 and number1 == 9:
            print("{}{}".format(number, number1))
        else:
            print("{}{}".format(number, number1), end=", ")
