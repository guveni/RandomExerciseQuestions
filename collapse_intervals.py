# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def collapse_intervals(input_arr):
    if not input_arr:
        return

    start = input_arr[0]
    prev = input_arr[0]

    for i in xrange(1, len(input_arr)):
        item = input_arr[i]
        if item == prev + 1:
            prev = item
        else:
            to_be_printed = "{}-{}".format(start,prev)
            if start == prev:
                to_be_printed = "{}".format(start)
            print to_be_printed
            start = item
            prev = item

    if item != prev + 1:
        to_be_printed = "{}-{}".format(start, prev)
        if start == prev:
            to_be_printed = "{}".format(start)
        print to_be_printed

input_arr = [1,3,4,5,8,9,10,40,41,42,43,60,61,70]

collapse_intervals(input_arr)