# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


input_array = [2, 3, 1, 0, 2, 5, 3]


def swap(input_array, first_item, second_item):
    temp = input_array[first_item]
    input_array[first_item] = input_array[second_item]
    input_array[second_item] = temp


def find_duplicate(input_array):
    if input_array == None or len(input_array) < 2:
        return None

    for i in xrange(len(input_array)):
        index = i
        while index != input_array[index]:
           if input_array[input_array[index]] == input_array[index]:
               return input_array[index]
           else:
               swap(input_array, index, input_array[index])

    return None

print find_duplicate(input_array)