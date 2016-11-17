# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


def is_palindrom(input_str):
    if input_str == '' and len(input_str) < 2:
        return False

    start = 0
    end = len(input_str) - 1

    while start <= end:
        if input_str[start] != input_str[end]:
            return False
        start += 1
        end -= 1

    return True


print is_palindrom('palindrome')
print is_palindrom('pap')
print is_palindrom('pa')
print is_palindrom('pp')
