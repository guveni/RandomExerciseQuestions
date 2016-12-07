# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'guven'


class CharTreeNode(object):
    """
    Tree node that has value as a char
    """

    def __init__(self, char_value, is_word_ending=False):
        self.is_word_ending = is_word_ending
        self.children = {}
        self.char_value = char_value

    def get_child(self, char):
        return self.children.get(char, None)

    def add_child(self, char, node):
        self.children[char] = node


def _add_word(root, word):
    if len(word) == 0:
        root.is_word_ending = True
        return
    else:
        c_node = root.get_child(word[0])
        if not c_node:
            root.add_child(word[0], CharTreeNode(word[0]))
            c_node = root.get_child(word[0])
        _add_word(c_node, word[1:])


class CharTree(object):
    """
    The word dictionary tree
    """

    def __init__(self, dict_list):
        self.root = CharTreeNode('root')
        for word in dict_list:
            _add_word(self.root, word)

    def process_input(self, input_str):
        result = []
        inp_len = len(input_str)
        index = 0
        while index < inp_len:
            last_word = None
            start_index = index
            last_word_index = index
            c_node = self.root
            while index < inp_len and c_node.get_child(input_str[index]):
                c_node = c_node.get_child(input_str[index])
                if c_node.is_word_ending :
                    last_word = c_node
                    last_word_index = index
                index += 1
            if last_word:
                result.append(input_str[start_index:last_word_index+1])
            index = last_word_index + 1
        return result


    def does_word_exist(self, word):
        # todo
        pass


def recover_text(text_str, word_dict_list):
    """

    :param text_str:
    :param word_dict_list:
    :return:
    """
    # tyzpe checks
    # none and length checks

    if not text_str or not word_dict_list:
        return None  # can be handled better

    word_tree = CharTree(word_dict_list)

    result = word_tree.process_input(text_str)
    if result:
        return " ".join(result)  # check whether the word order is kept

    return None

word_dict = ['the', 'these', 'old', 'green', 'grass', 'days']
input_str = 'theoldgreengrassdays'

print recover_text(input_str, word_dict)
