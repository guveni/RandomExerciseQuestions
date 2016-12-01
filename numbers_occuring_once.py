# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Let’s assume all numbers except two occur twice in an array. How do you get those two numbers to occur only once
    in O(n) time and O(1) space? For example, only two numbers, 4 and 6, in the array {2, 4, 3, 6, 3, 2, 5, 5} occur
    once, and the others numbers occur twice. Therefore, the output should be 4 and 6.
"""
__author__ = 'guven'


def get_singles(inp_arr):
    result = []
    if not inp_arr:
        return result

    xor_sum = 0

    for i in xrange(len(inp_arr)):
        xor_sum =  xor_sum ^ inp_arr[i]

    flag = 1
    while (xor_sum & flag) == 0:
        flag = flag << 1

    part1 = []
    part2 = []

    for i in xrange(len(inp_arr)):
        if inp_arr[i] & flag:
            part1.append(inp_arr[i])
        else:
            part2.append(inp_arr[i])

    res1 = 0
    res2 = 0

    for i in xrange(len(part1)):
        res1 = res1 ^ part1[i]

    for i in xrange(len(part2)):
        res2 = res2 ^ part2[i]

    return res1, res2

inp_arr = [2, 4, 3, 6, 3, 2, 5, 5]

print get_singles(inp_arr)