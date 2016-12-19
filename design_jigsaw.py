# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""



"""
__author__ = 'guven'

from enum import Enum

_BOARD_SIZE = 8

class Direction(Enum):
    up = 1
    right = 2
    down = 3
    left = 4

class EdgeType(object):
    flat = 1
    corner = 2
    inner = 3

class Edge(object):
    def __init__(self, parent, direction, edge_type):
        self.direction = direction
        self.parent = parent
        self.edge_type = edge_type

    def does_match(self, edge):
        pass


class Piece(object):
    def __init__(self):
        self.edges = []
        #todo


class Board(object):
    def __init__(self, solution):
        self.solution = solution
        self.pieces = [[None for x in xrange(_BOARD_SIZE)] for y in xrange(_BOARD_SIZE)]


