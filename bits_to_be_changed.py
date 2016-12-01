# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def count_bits(num):
    if num < 0:
        return 0
    count = 0
    while num:
        count += 1
        num = num & (num - 1)
    return count

def count_diff_bits(num1, num2):
    if num1 < 0 or num2 < 0:
        return -1

    big = num1 if num1 > num2 else num2
    small = num2 if num1 > num2 else num1

    diff = big ^ small

    return count_bits(diff)

print count_diff_bits(10, 13)
print count_bits(10)