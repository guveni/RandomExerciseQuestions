# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

This is also something to discuss with your interviewer, but here are some ideas:
• Signing online and offline.
• Add requests (sending, accepting, and rejecting).
• Updating a status message.
• Creating private and group chats.
• Adding new messages to private and group chats.
This isjust a partial list. If you have more time, you can add more actions.

    message
    user
    chat
"""
__author__ = 'guven'


from enum import Enum

class Message(object):
    def __init__(self, sender, receiver, text):
        self.text = text
        self.has_read = False
        self.sender = sender
        self.receiver = receiver

    def read_message(self):
        self.has_read = True
        return self.text

class Chat(object):
    def __init__(self):
        self.users = []
        self.messages = []

    def get_users(self):
        return  self.users

    def add_user(self, user):
        pass

    def remove_user(self , user):
        pass

    def add_message(self, message):
        pass


class Request(object):
    def __init__(self, chat_manager):
        self.chat_manager = chat_manager

    def accept(self):
        pass
    def reject(self):
        pass


class UserStatus(Enum):
    offline = 1
    online = 2


class User(object):
    def __init__(self, name, password):
        self.password = password
        self.name = name
        self.friends = []
        self.requests = []
        self.user_status = UserStatus.offline
        self.chats = []

    def add_requests(self):
        pass

    def add_friend(self, user):
        pass

    def remove_friend(self, user):
        pass



class UserManager(object):
    def __init__(self):
        self.user = []
        self.friend_requests = []

    def send_friend_request(self):
        pass


class ChatManager(object):
    def __init__(self):
        self.chats = {}


class ChatServer(object):
    def __init__(self):
        self.chat_manager = ChatManager()
        self.user_manager = UserManager()


