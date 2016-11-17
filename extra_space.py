# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'

def replace_blank(char_list):
    end = -1
    counter = 0

    if char_list == None or len(char_list) < 1:
        return None

    for i in  xrange(len(char_list)):
        cChar = char_list[i]
        if cChar == ' ':
            counter += 1
        elif cChar== '':
            end = i-1
            break

    new_end = end + 2 * counter
    if end == -1 or new_end > len(char_list):
        raise ValueError('Not enough space given!')

    while end >= 0 and new_end >= 0:
        while end >= 0 and new_end >= 0 and char_list[end] != ' ':
            char_list[new_end] = char_list[end]
            new_end -= 1
            end -= 1
        if new_end < 2:
            break
        char_list[new_end] = '0'
        new_end -= 1
        char_list[new_end] = '2'
        new_end -= 1
        char_list[new_end] = '%'
        new_end -= 1
        end -= 1

    return char_list

char_list = ['W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '', '', '', '']

char_list2 = ['W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', ' ', '', '', '', '', '', '']

char_list3 = [' ','W', 'e', ' ', 'a', 'r', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '', '', '', '', '', '']

char_list3 = [' ', ' ',  ' ',  '', '', '', '', '', '', '']

print replace_blank(char_list)

print replace_blank(char_list2)

print replace_blank(char_list3)
