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
    if not root:
        return None

    new_root = None
    n_c_node = None
    c_node = root

    while c_node:
        temp = ListNode(c_node.value)
        if not n_c_node:
            new_root = temp
            n_c_node = temp
        else:
            n_c_node.next = temp
            n_c_node = n_c_node.next

        temp.next = c_node.next
        c_node.next = temp
        c_node = temp.next

    print 'copied : first'

    c_node = root
    while c_node:
        temp = c_node.next
        temp.arbitrary = c_node.arbitrary
        if temp.arbitrary:
            temp.arbitrary = temp.arbitrary.next
        c_node = temp.next

    c_node = root
    while c_node:
        temp = c_node.next
        c_node.next = temp.next
        c_node = c_node.next

    return new_root


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
