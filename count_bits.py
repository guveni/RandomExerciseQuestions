# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

def count_bits(num):
    result = 0
    while num:
        if num & 1:
            result += 1
        num = num >> 1
    return result



def count_bits2(num):
    count = 0
    while num:
        count += 1
        num = num & (num-1)
    return count

print count_bits(10)
print count_bits2(10)

def check_if_power_of_two(num):
    if num <= 0:
        return False

    return num & (num -1) == 0

print check_if_power_of_two(2)

print check_if_power_of_two(20)