# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'
from random import randint

def swap(input_array, first, second):
    temp = input_array[first]
    input_array[first] = input_array[second]
    input_array[second] = temp

def partition(input_array, start, end):
    pivot = start + randint(0,end-start)
    swap(input_array, pivot,end)

    pre_index = start - 1
    for i in xrange(start, end):
        if input_array[end] > input_array[i]:
            pre_index += 1
            swap(input_array, i , pre_index)

    pre_index += 1
    swap(input_array, pre_index, end)
    return  pre_index

def quicksort_core(input_array, start, end):
    if end<=start or start < 0 or end > len(input_array):
        return

    pivot = partition(input_array, start, end)
    quicksort_core(input_array, start, pivot-1)
    quicksort_core(input_array, pivot +1 , end)
    return

def quicksort(input_array):
    if input_array == None:
        return
    quicksort_core(input_array, 0, len(input_array)-1)


input_array = [25,50,40,45,35,75]
quicksort(input_array)
print input_array

input_array = [25,50,40]
quicksort(input_array)
print input_array

input_array = [25]
quicksort(input_array)
print input_array
