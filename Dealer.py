__author__ = 'ericpark'

from Card import Card
from random import shuffle
from DealerStrategy import move

class Dealer(object):

    netCash = 0
    deck = []

    def __init__(self, numOfDecks=6):
        for i in range(0, numOfDecks):
            for suit in range(0, len(Card.suit_names)):
                for rank in range(0, len(Card.rank_names)):
                    self.deck.append(Card(suit, rank))
        self.shuffle_deck()

    def __str__(self):
        return "Dealer has made " + str(self.netCash)

    #TODO: Shuffle properly
    def shuffle_deck(self):
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
    #    for i in range(0, len(self.deck)):
    #        print self.deck[i]

    #Returns two cards from the shuffled deck
    def deal_hand(self):
        newHand = []
        newHand.append(self.deck.pop(0))
        newHand.append(self.deck.pop(0))
        return newHand


    #Returns next card in the shuffled deck
    def deal_card(self):
        nextCard = self.deck.pop(0)
        return nextCard

    def dealer_move(self, hand):
        return move(hand)