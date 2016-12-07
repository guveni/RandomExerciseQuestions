# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Please implement a function that gets the minimal number of coins with values v 1 , v 2 , ..., v n , to
make change for an amount of money with value t. There are an infinite number of coins for each value v i .
For example, the minimum number of coins to make change for 15 out of a set of coins with values 1, 3, 9, 10 is
3. We can choose two coins with value 3 and a coin with value 9. The number of coins for other choices should be
greater than 3.
"""

__author__ = 'guven'

def get_min_count(total, coins):
    if total < 0 or not coins:
        return -1

    row_len = len(coins) + 1
    column_len = total + 1

    matrix = [[0 for x in xrange(column_len)] for y in xrange(row_len)]

    for i in xrange(0, row_len):
        matrix[i][0] = i

    for i in xrange(0, column_len):
        matrix[0][i] = i

    for x in xrange(1, row_len):
        for y in xrange(1, column_len):
            pass

print get_min_count(15, [1,3,9,10])


if []:
    print 'sikerim BR i'
