# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


def bucket_sort(input_array, start, end):
    if input_array == None and len(input_array) < 2:
        return
    array_length = end-start
    bucket = [0] * array_length

    for item in input_array:
        bucket[start + input_array[item]] += 1

    index = 0
    for i in xrange(array_length):
        for j in xrange():
