# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


class Node():
    def __init__(self, value):
        self.next_node = None
        self.back_node = None
        self.value = value


def reverse_linked_list(root_node):
    if root_node == None:
        return None

    pass


def print_linked_list(root_node):
    temp = root_node
    while temp:
        print temp.value
        temp = temp.next_node


