# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'

def swap(input_array, first_index, second_index):
    temp = input_array[first_index]
    input_array[first_index] = input_array[second_index]
    input_array[second_index] = temp


def find_multiple_duplicates(input_array):
    if input_array ==  None or len(input_array) < 2:
        raise ValueError()

    index = 0
    while index < len(input_array) :
        while index != input_array[index]:
            if input_array[index] < 0 or input_array[index] >= len(input_array):
                raise ValueError()
            if input_array[index] == input_array[input_array[index]]:
                return input_array[index]
            swap(input_array, index,  input_array[index])
        index += 1

    raise  ValueError()

input_array = [2, 3, 1, 0, 2, 5, 3]

print find_multiple_duplicates(input_array)
