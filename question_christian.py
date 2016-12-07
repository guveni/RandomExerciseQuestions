# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


from os import walk


FILE_PATH = ''
TARGET_CODE = '5'
SEPERATOR = '_'

def get_line_code(the_line_string):
    params = the_line_string.split(SEPERATOR)
    if params:
        return None
    return params[len(params)-1]

def process_report_line(report_line):
    return report_line.split(SEPERATOR)

def get_response_time(the_line_string):
    params = the_line_string.split(SEPERATOR)
    time = int(params[len(params)-2])
    return time

def get_error_code_count(row_list):
    if not row_list:
        return
    failed_calls = 0
    for row in row_list:
        code = get_line_code(row)
        if code.startswith(TARGET_CODE):
            failed_calls += 1

    return failed_calls


def get_longest_calls(row_list):
    call_no = 10
    if not row_list:
        return
    response_times = []
    for row in row_list:
        time = get_response_time(row)
        response_times.append(time)
    response_times.sort(reverse=True)
    call_no = call_no if len(response_times) > call_no else len(response_times)

    return response_times[:call_no]

test_lines = [
    'date1_ip1_cid1_',
]

print get_error_code_count(test_lines)

