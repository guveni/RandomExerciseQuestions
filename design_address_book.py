# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""


design address book
	get info based on name
	get info based on number

address
entry
    name
    number
    address



"""
__author__ = 'guven'

class Address(object):
    def __init__(self, name, number, address):
        self.address = address
        self.name = name
        self.number = number


class AddressBook(object):
    def __init__(self):
        self.name_index = {}
        self.number_index = {}

    def add_address(self, address):
        self.name_index[address.name] = address
        self.number_index[address.number] = address
