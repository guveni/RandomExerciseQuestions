# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def multiply_without_recursion(x,y):
    x_flag = False
    if x < 0:
        x_flag = True
        x = -x
    y_flag = False
    if y < 0:
        y_flag = True
        y = -y

    is_neg = False
    if x_flag and y_flag:
        is_neg = False
    elif x_flag or y_flag:
        is_neg = True

    result = core(x,y)
    if is_neg:
        result = -result
    return result

def core(x,y):
    if y == 0:
        return 0

    return x + core(x,y-1)

print multiply_without_recursion(5,4)
print multiply_without_recursion(5,-4)
print multiply_without_recursion(-5,4)
print multiply_without_recursion(0,6)