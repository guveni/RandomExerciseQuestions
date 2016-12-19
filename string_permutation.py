# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'



def permutate(input_str):

    if not input_str:
        return

    char_arr = [char for char in input_str]
    permutate_core(char_arr, 0)


def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def permutate_core(char_arr, start):
    if start == len(char_arr):
        print ''.join(char_arr)
        return

    for i in xrange(start, len(char_arr)):
        swap(char_arr, start, i)
        permutate_core(char_arr, start+1)
        swap(char_arr, start, i)



permutate('abc')