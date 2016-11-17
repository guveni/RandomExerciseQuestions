# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def replace_blank(input_str):
    if input_str == None or len(input_str) < 1:
        return input_str
    if not isinstance(input_str, basestring):
        raise ValueError()

    counter = 0
    for c in input_str:
        if c == ' ':
            counter += 1



input_str = ['W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '.', '', '', '']
