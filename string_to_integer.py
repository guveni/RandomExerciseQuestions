# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def string_to_integer(str_input):
    pass


def get_digit(cur_char):
    try:
        cur_char = ord(cur_char)
    except:
        return -1
    if cur_char >= ord("0") and cur_char <= ord("9"):
        return cur_char - ord("0")
    return -1


print get_digit("8")

for i in xrange(0,10):
    print str(i) + ' : ' +str(ord(str(i)))