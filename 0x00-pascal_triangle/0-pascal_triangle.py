#!/usr/bin/python3
"""
This code defines a function that returns a list of lists of integers that represents the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    parameters that will be used:
    n [int]: Pascal triangle rows that will be created

    to return:
        [list of lists of integers]: this represents the Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n is an integer")
    triangle = []
    if n <= 0:
        return triangle
    previous = [1]
    for row_index in range(n):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        triangle.append(rowlist)
    return triangle
