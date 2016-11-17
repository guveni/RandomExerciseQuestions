# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def solution(N):
    # write your code in Python 2.7
    result = 0
    temp = 0

    is_recording = False
    while N > 0:
        if N & 1 == 1:
            is_recording = True
            if temp > result:
                result = temp
            temp = 0
        else:
            if is_recording:
                temp += 1
        N = N >> 1
    if temp > result:
        result = temp

    return result

print solution(1041)