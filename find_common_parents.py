# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_common_parents(root, first, second):
    if not root or not first or not second:
        return None

    f_path = []
    path_finder(root, f_path, first)
    s_path = []
    path_finder(root, s_path, second)

    index1 = 0
    index2 = 0

    common = None
    while index1 < len(f_path) and index2 < len(s_path) and f_path[index1].value == s_path[index2].value:
        common = f_path[index1]
        index1 += 1
        index2 += 1

    return common


def path_finder(root, path, target):
    if not root:
        return False

    path.append(root)

    if root.value == target.value or path_finder(root.left, path, target) or path_finder(root.right, path, target):
        return True

    path.pop()

    return False


root1 = TreeNode(10)
second1 = TreeNode(20)
root1.left = second1
second2 = TreeNode(21)
root1.right = second2


common_node = find_common_parents(root1, second1, second2)
if common_node:
    print  common_node.value