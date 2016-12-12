# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Design the data structures for a generic deck of cards.
    Explain how you would sub - class it to implement particular card games.


    hand
        get hand
    deck
        cards
    card
        suit
        value

"""
__author__ = 'guven'
from enum import Enum


class Suit(Enum):
    hearts = 1
    spades = 2
    clubs = 3
    diamonds = 4


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_available = True

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self.value = value


class BlackJackCard(Card):
    def __init__(self, value, suit):
        Card.__init__(value, suit)

    @property
    def value(self):
        val = self.value
        if val == 1:
            return val
        if val < 10:
            return val
        return 10


class Deck(object):
    def __init__(self):
        self.cards = []
        self.dealt_index = 0

    def deal_card(self):
        pass

    def deal_hand(self):
        pass

    def shuffle(self):
        pass

    def remaining_cards_num(self):
        pass


class Hand(object):

    def __init__(self):
        self.cards = []

    def score(self):
        pass

    def add_card(self, card):
        pass

if __name__ == '__main__':
    card = Card(9, Suit.clubs)

    print card