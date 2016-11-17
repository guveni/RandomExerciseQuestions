# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


class Node():
    def __init__(self, value, next_node = None):
        self.next_node = next_node
        self.value = value


def detect_cycle(root_node):
    if root_node == None:
        return False

    slow = root_node
    fast = root_node.next_node
    if fast:
        fast = fast.next_node

    while(fast and fast != slow):
        slow = slow.next_node
        fast = fast.next_node
        if fast:
            fast = fast.next_node


    if fast and fast == slow:
        return True

    return False


def test1():
    root_node = Node(1)
    second_node = Node(2)
    root_node.next_node = second_node
    third_node = Node(3)
    second_node.next_node = third_node
    fourth_node = Node(4,root_node)
    third_node.next_node = fourth_node

    print detect_cycle(root_node)

def test2():
    root_node = Node(1)
    second_node = Node(2)
    root_node.next_node = second_node
    third_node = Node(3)
    second_node.next_node = third_node
    fourth_node = Node(4)
    third_node.next_node = fourth_node

    print detect_cycle(root_node)

test1()
test2()
