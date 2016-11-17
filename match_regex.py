# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
How do you implement a function to match regular expressions with ‘.’ and ‘*’ in patterns? The
character ‘.’ in a pattern matches a single character, and ‘*’ matches zero or any number of characters preceding
it. Matching means that a string fully matches the pattern where all characters in a string match the whole pattern.
For example, the string “aaa” matches the pattern “a.a” and the pattern “ab*ac*a”. However, it does not match
the pattern “aa.a” nor “ab*a”.

"""
__author__ = 'guven'


def match_regex(input_str, regex_statement):
    if input_str == None or regex_statement == None or len(input_str) < 1 or len(regex_statement) < 1:
        raise ValueError("Invalid argument!")

    return consume(input_str, 0, regex_statement,0)


def consume2(input_str, input_index, regex_statement, regex_index):
    if len(input_str)==input_index and len(regex_statement) == regex_index:
        return True
    if len(input_str)==input_index or len(regex_statement) == regex_index:
        return False

    if input_str[input_index] == regex_statement[regex_index] or regex_statement[regex_index] == '.':
        return consume2(input_str, input_index+1, regex_statement, regex_index+1)

    return False

def consume(input_str, input_index, regex_statement, regex_index):
    if len(input_str)==input_index and len(regex_statement) == regex_index:
        return True
    if len(input_str)!=input_index and len(regex_statement) == regex_index:
        return False

    if regex_index + 1 < len(regex_statement) and regex_statement[regex_index+1] == '*':
        if len(input_str)==input_index or (regex_statement[regex_index] != input_str[input_index] and regex_statement[regex_index] != '.'):
            return consume(input_str, input_index, regex_statement, regex_index + 2)
        elif regex_statement[regex_index] == '.' or regex_statement[regex_index] == input_str[input_index]:
            return consume(input_str, input_index+1, regex_statement, regex_index)

    if input_str[input_index] == regex_statement[regex_index] or regex_statement[regex_index] == '.':
        return consume(input_str, input_index+1, regex_statement, regex_index+1)

    return False

#test cases
def wrapper(num, bool_flag, expected):
    result = ''
    if bool_flag == expected:
        result = 'successfull'
    else:
        result = 'failed'
    print 'test case {} is {}'.format(num, result)


wrapper(1, match_regex('aaa','a.a'),True)
wrapper(2, match_regex('aaa','aaa'),True)
wrapper(3, match_regex('aaa','aa'),False)
wrapper(4, match_regex('aaa','a*'),True)
wrapper(5, match_regex('aaa','.*'),True)
wrapper(6, match_regex('aaa','a.*'),True)
