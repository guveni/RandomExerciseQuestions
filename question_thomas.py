# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


def check_raise_error(the_input, the_type):
    assert isinstance(the_input, type(the_type))

class CharTreeNode(object):
    """
    Tree node that has value as a char
    """
    def __init__(self,char_value, is_word_ending = False):
        check_raise_error(char_value,basestring)
        self.char_value = char_value
        self.is_word_ending = is_word_ending
        self.children = {}
    def get_child(self, char):
        return self.children.get(char, None)
    def add_child(self, cahr, node):
        self.children[cahr] = node


class CharTree(object):
    """
    The word dictionary tree
    """

    def __init__(self, dict_list):
        self.root = None
        for word in dict_list:
            self._add_word(word)

    def process_input(self, input_str):
        result = []
        inp_len = len(input_str)
        for i in xrange(inp_len):
            start_node = self.root.get_child(inp_len[i])
            if start_node:
                j = i + 1
                while j < inp_len and not word_tree.does_word_exist(inp_len[i:j]):
                    j += 1
                j = j - 1
                if not word_tree.does_word_exist(inp_len[i:j]):
                    continue
                greedy_index = j + 1
                while greedy_index < inp_len and word_tree.does_word_exist(inp_len[i:greedy_index]):
                    greedy_index += 1

    def _add_word(self, word):
        check_raise_error(word, basestring)
        #todo

    def does_word_exist(self,word):
        #todo
        pass


def recover_text(text_str, word_dict_list):
    """

    :param text_str:
    :param word_dict_list:
    :return:
    """
    # tyzpe checks
    # none and length checks
    check_raise_error(text_str, basestring)
    check_raise_error(word_dict_list, list)

    if not text_str or not word_dict_list:
        return None # can be handled better

    word_tree = CharTree(word_dict_list)

    result = word_tree.process_input(text_str)
    if result:
        return " ".join(result) # check whether the word order is kept

    return None

