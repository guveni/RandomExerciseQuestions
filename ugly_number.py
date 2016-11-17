# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        ugly_numbers = [1]
        two_index = 0
        third_index = 0
        five_index = 0

        while len(ugly_numbers) < n:
            two_result = ugly_numbers[two_index] * 2
            third_result = ugly_numbers[third_index] * 3
            five_result = ugly_numbers[five_index] * 5
            result = min(two_result, third_result, five_result)
            if result == two_result:
                two_index += 1
            if result == third_result:
                third_index += 1
            if result == five_result:
                five_index += 1
            ugly_numbers.append(result)

        if len(ugly_numbers) < 1:
            return 0

        return ugly_numbers[len(ugly_numbers) - 1]