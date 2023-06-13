#!/usr/bin/python3
"""Define the pescil triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    row = [1]
    tmp = [0]
    p = []
    if n < 0:
        return p
    for i in range(n):
        p.append(row)
        row = [l+r for l, r in zip(row + tmp, tmp + row)]
    return p
