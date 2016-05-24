__author__ = 'ericpark'

from Card import Card
from random import shuffle

class Dealer(object):

    netCash = 0
    deck = []

    def __init__(self, numOfDecks=6):
        for i in range(0, numOfDecks):
            for suit in range(0, len(Card.suit_names)):
                for rank in range(0, len(Card.rank_names)):
                    self.deck.append(Card(suit, rank))
        self.shuffleDeck()

    def __str__(self):
        return "Dealer has made " + str(self.netCash)

    #TODO: Shuffle properly
    def shuffleDeck(self):
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
        for i in range(0, len(self.deck)):
            print self.deck[i]

def dealHand(players):
    return ""

def dealCard():
    return ""

