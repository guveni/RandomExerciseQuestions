# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


def print_spirally(matrix):

    if not matrix:
        return

    length = len(matrix)

    for row in matrix:
        if len(row) != length:
            return

    for i in xrange(length / 2):

        for j in xrange(i, length-i):
            print matrix[i][j]

        for j in xrange(i+1, length-i):
            print matrix[j][length-i-1]

        for j in xrange(length-i-2, i-1, -1):
            print matrix[length-i-1][j]

        for j in xrange(length-i-2, i, -1):
            print matrix[j][i]



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print_spirally(matrix)
