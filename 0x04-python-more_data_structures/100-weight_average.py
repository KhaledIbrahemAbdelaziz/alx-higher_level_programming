#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average
    of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0
    sums = 0
    av = 0
    for i in my_list:
        sums += i[0] * i[1]
        av += i[1]
    return (sums / av)
