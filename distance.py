# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'

def get_min_of_three(o1,o2,o3):
    first = o1 if o1 < o2 else o2
    result = first if first < o3 else o3
    return result


def calculate_dist(str1, str2):
    if not str1 or not str2:
        return -1

    len1 = len(str1)+1
    len2 = len(str2)+1
    matrix = [[0 for x in xrange(len1)] for y in xrange(len2)]

    for i in xrange(1,len1):
        matrix[0][i] = i


    for i in xrange(1,len2):
        matrix[i][0] = i

    for y in xrange(1, len1):
        for x in xrange(1, len2):
            c1 = str1[y-1]
            c2 = str2[x-1]
            if c1 == c2:
                matrix[x][y] = matrix[x-1][y-1]
            else:
                opt1 = matrix[x-1][y]
                opt2 = matrix[x][y-1]
                opt3 = matrix[x-1][y-1]
                matrix[x][y] = get_min_of_three(opt1, opt2, opt3) +1

    return matrix[len2-1][len1-1]

print calculate_dist('saturday','sunday')
