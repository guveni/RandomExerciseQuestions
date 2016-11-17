# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

"""
1 2 8 9
2 4 9 12
4 7 10 13
6 8 11 15
"""

input_array = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]

def search_diagonally(input_array, target):
    if input_array==None or len(input_array) < 1:
        return None

    length = len(input_array[0])
    for i in xrange(1, len(input_array)):
        if length != len(input_array[i]):
            raise ValueError("wrong input!")

    row = len(input_array)-1
    column = 0

    while row >= 0 and column < len(input_array[0]):
        item = input_array[row][column]

        if item == target:
            return True
        elif item < target:
            column += 1
        else:
            row -= 1

    return False

print search_diagonally(input_array, 9)