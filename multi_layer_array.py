# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


input_array = [
    [1,3,5],
    [7,9,11],
    [13,15,17]
]


def find_in_matrix(input_array, target):
    if input_array==None or len(input_array) < 1:
        return None

    length = len(input_array[0])
    for i in xrange(len(input_array)):
        if length != len(input_array[i]):
            raise ValueError("wrong input!")

    start = 0
    end = len(input_array) * len(input_array[0]) - 1

    while start <= end:
        mid = start + (end - start) / 2
        row = (mid / len(input_array))
        column = (mid % len(input_array[0]))

        item = input_array[row][column]
        if item == target:
            return True
        elif item > target:
            end = mid -1
        else:
            start = mid + 1
    return False


print find_in_matrix(input_array, 12)