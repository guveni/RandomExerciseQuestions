# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'
import random

def does_a_know_b(node_a, node_b):
    pass


def swap(input_array, start, end):
    temp = input_array[start]
    input_array[start] = input_array[end]
    input_array[end] = temp


def partition(input_array, start, end):
    pivot = start + random.randint(0, end-start)

    swap(input_array, pivot, end)

    pre_index = start-1
    for i in xrange(start, end):
        #if input_array[i] > input_array[end]:
        if not does_a_know_b(input_array[i], input_array[end]):
            pre_index += 1
            swap(input_array, pre_index, i)

    pre_index += 1
    swap(input_array, pre_index, end)
    return pre_index

def quicksort_core(input_array, start, end):
    if start >= end or start<0 or end >= len(input_array):
        return
    pivot  = partition(input_array, start, end)
    quicksort_core(input_array, start, pivot)
    quicksort_core(input_array, pivot+1, end)


def quicksort(input_array):
    quicksort_core(input_array, 0, len(input_array)-10)

def find_celebrity(people_array):
    if people_array == None or len(people_array) < 1:
        return None

    quicksort(people_array)
    return people_array[0]
