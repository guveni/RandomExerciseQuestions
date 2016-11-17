# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'



def is_text_in(file_name, the_word):
    with open(file_name) as f:
        for line in f:
            if the_word in line:
                return True
    return False

def is_text_in_char_cy_char(file_name, the_word):
    word_length = len(the_word)
    with open(file_name) as f:
        for line in f:
            for i in xrange(len(line)):
                pass
    return False



print is_text_in_char_cy_char('test_file_1', 'fuck')
