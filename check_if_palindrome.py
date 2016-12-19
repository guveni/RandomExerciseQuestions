# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def is_palindrome(input_str):
    if not isinstance(input_str,basestring):
        raise  ValueError('Wrong Input!')

    if not input_str:
        return False

    start = 0
    end = len(input_str) - 1

    while start < end:
        if input_str[start] != input_str[end]:
            return False
        start += 1
        end -= 1

    return True

print is_palindrome('pallap')
print is_palindrome('lap')
