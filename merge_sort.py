# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


def swap(array, index1 , index2):
    #print '{} and {} swapped'.format(array[index1],array[index2])
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp

def merge(start1, start2, end , array):
    counter = 0
    begin = start1
    middle_index = start2

    while start1<start2 and start2<=end :
        if array[start1] > array[start2]:
            counter = counter + 1
            swap(array, start1, start2)
        start1 += 1
        if start2 == start1:
            start2 += 1
    return counter

def merge_sort(start, end, array):
    if start>= end :
        return 0
    midIndex = (start + end) /2
    left = merge_sort(start, midIndex, array)
    right = merge_sort(midIndex+1, end, array)
    mid = merge(start, midIndex+1, end, array)
    return  mid + left + right

def count_inversions(a):
    result = merge_sort(0, len(a)-1, a)
    print a
    return result
"""
print count_inversions([2,1,3])
print count_inversions([2,1,3,1,2])
print count_inversions([2,4,1])
print count_inversions([3,2,1])
"""
print count_inversions([8, 56786, 354345, 2, 234, 342])
#print count_inversions([354345,56786,8,234,2,342,567,86,789,123124,568,789789])
