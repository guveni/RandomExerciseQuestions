# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Besides 2 and 10, numbers can be converted with other bases. For instance, the time system has 60 as its base to
     record seconds, minutes, and hours. The following problem is an interesting interview question about numbers
     with uncommon bases: in Microsoft Excel, “A” stands for the first column, “B” for the second column, ..., “Z”
     for the 26th column, “AA” for the 27th column, “AB” for the 28th column, and so on. Please write a function to
     get the column index according to a given string.
"""
__author__ = 'guven'


def get_char_value(c_char):
    val = ord(c_char)
    if val <= 90 and val >= 65:
        return val - 64
    return -1

def get_exp(num, exponent):
    if exponent < 1:
        return 1
    result = num
    for i in xrange(1, exponent):
        result *= result
    return result


def get_column_index(input_str):
    result = 0
    if not input_str:
        return result

    index = 0
    for i in xrange(len(input_str)-1, -1, -1):
        value = get_char_value(input_str[i])
        result += get_exp(26, index) * value
        index += 1

    return result

print get_column_index("AA")
print get_column_index("BA")
#print ord("A")
#print ord("Z")