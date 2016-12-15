# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Imagine you have a call center with three levels of employees: respondent,
    manager, and director. An incoming telephone call must be first allocated
    to a respondent who is free. If the respondent can't handle the call,
     he or she must escalate the call to a manager. If the manager is not
     free or notable to handle it, then the call should be escalated to a director.
     Design the classes and data structures for this problem. Implement a method
     dispatchCaL L() which assigns a call to the first available employee.


employee
    respondent
    manager
    director
call


"""
__author__ = 'guven'
from enum import Enum


class Call(Enum):
    respondent = 1
    manager = 2
    director = 3

    def __init__(self, call_details):
        self.call_details = call_details

class Employee(object):
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.is_available = False
        self.call_center = None

    def can_handle_call(self, call):
        raise NotImplemented()


class CallCenter(object):
    def __init__(self, respondent, manager, director):
        self.respondent_list = respondent
        self.manager_list = manager
        self.director_list = director
        self.call_queue = [[],[],[]]

    def receive_call(self, call):
        pass

    def add_respondent_call_queue(self, call):
        pass

    def add_manager_call_queue(self, call):
        pass

    def add_director_call_queue(self, call):
        pass