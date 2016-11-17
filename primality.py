# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'

import math

def is_prime(num):
    if num <1:
        return False
    for i in xrange(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

print is_prime(12)

print is_prime(5)

print is_prime(7)
