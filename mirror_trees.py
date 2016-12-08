# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


class TreeNode(object):
    def __init__(self, value):
        self.value = str(value)
        self.left = None
        self.right = None


def traverse_tree(root):
    if not root:
        return ''

    left = traverse_tree(root.left)
    right = traverse_tree(root.right)

    return  left + root.value + right

def is_mirror_tree(root):
    if not root:
        return False

    tree_traversed  = traverse_tree(root)
    start = 0
    end = len(tree_traversed) - 1
    while start < end:
        if tree_traversed[start] != tree_traversed[end]:
            return False
        start += 1
        end -= 1

    return True


def is_symmetrical(root):
    if not root:
        return False



def mirror_tree(root):
    if not root:
        return

    temp = root.left
    root.left = root.right
    root.right = temp

    if root.left:
        mirror_tree(root.left)
    if root.right:
        mirror_tree(root.right)


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)

root.left.left = TreeNode(5)
root.left.right = TreeNode(7)

root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

print  traverse_tree(root)
mirror_tree(root)
print  traverse_tree(root)

"""
print is_mirror_tree(root)

root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(6)


root.left.left = TreeNode(5)
root.left.right = TreeNode(7)

root.right.left = TreeNode(7)
root.right.right = TreeNode(5)

print is_mirror_tree(root)
"""
