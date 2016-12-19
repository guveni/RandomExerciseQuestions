# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

OnlineReaderSystem
book
usermanager
user
library
display


"""
__author__ = 'guven'


class OnlineReaderSystem(object):
    def __init__(self):
        self.library = Library()
        self.display = Display()
        self.user_manager = UserManager()
        self.active_user = None
        self.active_book = None

    def user_log_in(self, name, password):
        user = self.user_manager.get_user_by_name(name)
        if not user.is_valid_passoword(password):
            return False
        self.active_user = user
        return True


class Library(object):
    def __init__(self):
        self.books_by_id = {}

    def get_book(self, book_id):
        return self.books_by_id.get(book_id, None)

    def add_book(self, book):
        self.books_by_id[book.id] = book


class Book(object):
    def __init__(self, id, info):
        self.id = id
        self.info = info


class Display(object):
    def __init__(self):
        self.current_book = None

    def show_book(self, book):
        self.current_book = book
        self._render()

    def turn_page_forward(self):
        pass

    def turn_page_backward(self):
        pass

    def _render(self):
        pass


class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.age = None
        self.address = None


class UserManager(object):
    def __init__(self):
        self.user_id_index = {}
        self.user_name_index = {}

    def add_user(self, user):
        pass

    def remove_user_by_id(self,user_id):
        pass

    def get_user_by_id(self,id):
        pass

    def get_user_by_name(self,name):
        pass

    def is_valid_passoword(self, name, password):
        user = self.user_name_index[name]
        return  user.password == password