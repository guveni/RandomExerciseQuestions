# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert_bst_to_ll(root):
    if not root:
        return None

    result = core_converter(root)

    return result


def core_converter(node):
    if not node :
        return None

    left = core_converter(node.left)
    right = core_converter(node.right)

    result = None

    node.left = left
    node.right = right