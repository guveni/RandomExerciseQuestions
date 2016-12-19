# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def check_if_graph_tree(root):
    if not root:
        return False

    q = deque()
    hash = set()
    hash.add(root.value)
    q.append(root)

    while len(q):
        first = q.popleft()
        for node in first.children:
            if node.value in hash:
                return False
            hash.add(node.value)
            q.append(node)

    return True


