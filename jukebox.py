# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    select music

"""
__author__ = 'guven'

from collections import deque
class Song(object):
    def __init__(self,song_id, song_name, song_info):
        pass

class PlayList(object):
    def __init__(self, song_ids):
        self.song_ids = song_ids
        self.song_queue = deque()

class Jukebox(object):
    def __init__(self, songs, playlists):
        self.playlists = playlists
        self.songs = songs

