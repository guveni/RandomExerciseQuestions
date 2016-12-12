# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_zig_zag(root):
    if not root:
        return

    q = deque()
    q.append(root)

    order = True

    level_items = []
    to_be_printed = 1
    next_level = 0

    while len(q):
        top = q.popleft()
        to_be_printed -= 1

        level_items.append(str(top.value))

        if top.left:
            q.append(top.left)
            next_level += 1

        if top.right:
            q.append(top.right)
            next_level += 1

        if to_be_printed == 0:
            if not order:
                level_items.reverse()

            print ' '.join(level_items)
            level_items = []
            order = not order
            to_be_printed = next_level

    if len(level_items):
        if not order:
            level_items.reverse()

        print ' '.join(level_items)

root = Node(8)
left = Node(6)
right = Node(10)

root.left = left
root.right = right

left.left = Node(5)
left.right = Node(7)

right.left = Node(9)
right.right = Node(11)

print_tree_zig_zag(root)