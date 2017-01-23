# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'

class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def is_sym(root):
    if not root:
        return False

    node_list = []
    print_tree_list(root, node_list)

    start = 0
    end = len(node_list) - 1

    while start < end:
        if node_list[start] != node_list[end]:
            return False
        start += 1
        end -= 1

    return  True

def print_tree_list(root, node_list):
    if not root:
        return

    print_tree_list(root.left, node_list)
    node_list.append(root.value)
    print_tree_list(root.right, node_list)


root = TreeNode(8)
left = TreeNode(6)
left.left= TreeNode(5)
left.right= TreeNode(7)
right = TreeNode(6)
right.left =TreeNode(7)
right.right =TreeNode(5)


root.left = left
root.right = right

print is_sym(root)

