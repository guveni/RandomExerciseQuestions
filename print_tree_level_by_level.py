# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

from collections import deque
from sys import stdout
#from __future__ import print_function

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree_levels(root):
    if not root:
        return

    q = deque()

    next_level = 0
    to_be_printed = 1
    q.append(root)

    while len(q):
        top = q.popleft()
        to_be_printed -= 1

        stdout.write(str(top.value) + ' ')

        if top.left:
            q.append(top.left)
            next_level += 1

        if top.right:
            q.append(top.right)
            next_level += 1

        if to_be_printed == 0:
            to_be_printed = next_level
            next_level = 0
            print ''

    stdout.flush()

root = Node(8)
left = Node(6)
right = Node(10)

root.left = left
root.right = right

left.left = Node(5)
left.right = Node(7)

right.left = Node(9)
right.right = Node(11)

print_tree_levels(root)