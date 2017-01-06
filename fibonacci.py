# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    0 1 1
"""
__author__ = 'guven'


def fib(nth):

    if nth < 1:
        raise ValueError('Invalid Input!')

    a = 1
    b = 0

    for i in xrange(1,nth):
        c = a + b
        a = b
        b = c

    return b

for i in xrange(1,10):
    print fib(i)