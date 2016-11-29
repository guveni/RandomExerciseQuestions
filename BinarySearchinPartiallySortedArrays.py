# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    When some elements at the beginning of an array are moved to the end, it becomes a rotation of the original array.
    Please implement a function to get the minimum number in a rotation of an increasingly sorted array.
    For example, the array {3, 4, 5, 1, 2} is a rotation of array {1, 2, 3, 4, 5}, of which the minimum is 1.

    1, 2, 3, 4, 5
    2, 3, 4, 5, 1
    5, 1, 2, 3, 4

    3, 4, 5, 1, 2

"""

__author__ = 'guven'


def find_min_rotated(input_array):

    if not input_array:
        return -1

    p1 = 0
    p2 = len(input_array)-1

    if input_array[p1] < input_array[p2]:
        return p1

    while p2 > p1 :
        if p2 - p1  == 1 :
            p2
        mid = p1 + (p2-p1)/2
        if mid > 0 and mid < len(input_array) and input_array[mid] < input_array[mid - 1] and input_array[mid] < input_array[mid + 1]:
            return mid
        if input_array[mid] < input_array[p2]:
            if input_array[mid] > input_array[p1]:
                p2 = mid - 1
            else:
                p2 = mid - 1
        else:
            if input_array[mid] > input_array[p1]:
                p1 = mid + 1
            else:
                p1 = mid + 1

    return p1

print find_min_rotated([1, 2, 3, 4, 5])

print find_min_rotated([5, 1, 2, 3, 4])
print find_min_rotated([4, 5, 1, 2, 3])

print find_min_rotated([3, 4, 5, 1, 2])
print find_min_rotated([2, 3, 4, 5, 1])
