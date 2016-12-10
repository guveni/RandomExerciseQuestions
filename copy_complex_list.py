# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.arbitrary = None


def copy_complex_list(root):
    copy_root = None
    if not root:
        return copy_root

    c_node = root
    while c_node:
        temp = ListNode(c_node.value)
        temp.next = c_node.next
        c_node.next = temp
        c_node = temp.next

    c_node = root
    while c_node:
        temp = c_node.next
        if c_node.arbitrary:
            temp.arbitrary = c_node.arbitrary.next
        c_node = temp.next

    copy_root = root.next
    c_node = root
    while c_node:
        temp = c_node.next
        c_node.next = temp.next
        if c_node.next:
            temp.next = c_node.next.next
        c_node = c_node.next

    return copy_root


first = ListNode(40)

second = ListNode(50)
first.next = second

third = ListNode(60)
first.next.next = third

fourth = ListNode(70)
first.next.next.next = fourth

fifth = ListNode(80)
first.next.next.next.next = fifth

first.arbitrary = fifth
fifth.arbitrary = second
second.arbitrary = fourth
fourth.arbitrary = third


copied_list = copy_complex_list(first)
print 'copied'
