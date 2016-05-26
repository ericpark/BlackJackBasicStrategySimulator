__author__ = 'ericpark'

from Card import Card
from random import shuffle
from DealerStrategy import move


class Dealer(object):

    netCash = 0
    deck = []

    def __init__(self, num_of_decks=6):
        for i in range(0, num_of_decks):
            for suit in range(0, len(Card.suit_names)):
                for rank in range(0, len(Card.rank_names)):
                    self.deck.append(Card(suit, rank))
        self.shuffle_deck()

    def __str__(self):
        return "Dealer has made " + str(self.netCash)

    # TODO Shuffle properly
    def shuffle_deck(self):
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
    #    for i in range(0, len(self.deck)):
    #        print self.deck[i]

    def deal_hand(self):
        """Returns two cards from the shuffled deck"""
        return [self.deck.pop(0), self.deck.pop(0)]

    def deal_card(self):
        """Returns next card in the shuffled deck"""
        next_card = self.deck.pop(0)
        return next_card

    @staticmethod
    def dealer_move(hand):
        return move(hand)
