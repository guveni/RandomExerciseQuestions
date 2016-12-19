# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

class StackNode(object):
    def __init__(self, maximum, value):
        self.maximum = maximum
        self.value = value


class MaxStack(object):
    def __init__(self):
        self._core_list = []

    def push(self, value):
        maximum = value
        if self._core_list:
            prev = self.max()
            if prev > maximum:
                maximum = prev
        self._core_list.append(StackNode(maximum=maximum, value=value))

    def pop(self):
        if not self._core_list:
            raise ValueError('No value exists!')

        value = self._core_list.pop().value
        return value

    def max(self):
        if not self._core_list:
            raise ValueError('No value exists!')

        return self._core_list[-1].maximum