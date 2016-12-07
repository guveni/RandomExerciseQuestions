# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'

SIZE = 8

class Board(object):

    def __init__(self):
        self.squares = [[ None for x in SIZE ] for y in SIZE ]
        #initialize board
        #done

    def canMove(self, pos1, pos2):
        #paramater check
        if not pos1 or not pos2:
            raise ValueError()

        #check if pos1 has an item
        item = self.squares[pos1.x][pos1.y]
        if not item:
            raise Exception('empty origin!')

        #parametrize here to check bounds only fdone for pos1
        if pos1.x < 0 or pos1.x >= SIZE:
            raise Exception('OOB!')

        dest_item = self.squares[pos2.x][pos2.y]
        if dest_item and item.color == dest_item.color:
            raise Exception('FF')

        return item.canMove(pos1, pos2)



class Piece(object):

    def __init__(self, color):
        self.color = color

    def canMove(self, pos1, pos2):
        raise NotImplemented()

class Horse(Piece):
    def __init__(self, color):
        Piece.__init__(self,color)

    def canMove(self, pos1, pos2):
        abs_x = abs(pos1.x - pos2.x)
        abs_y = abs(pos1.y - pos2.y)

        if (abs_x == 2 and abs_y == 1) or (abs_x == 1 and abs_y == 2):
            return True
        return False