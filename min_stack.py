# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

class StackNode(object):
    def __init__(self, value, cur_min):
        self.value = value
        self.cur_min = value if value < cur_min else cur_min

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(StackNode(value, self.min()))

    def pop(self):
        if not self.stack:
            raise ValueError()
        return self.stack.pop()

    def min(self):
        if not self.stack:
            raise ValueError()

        return self.stack[len(self.stack)-1].min
