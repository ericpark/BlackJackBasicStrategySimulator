__author__ = 'ericpark'

from Card import Card
from random import shuffle
from DealerStrategy import move
import time


class Dealer(object):

    netCash = 0
    deck = []
    hand = []

    def __init__(self, num_of_decks=6):
        for i in range(0, num_of_decks):
            for suit in range(0, len(Card.suit_names)):
                for rank in range(0, len(Card.rank_names)):
                    self.deck.append(Card(suit, rank))
        self.shuffle_deck()

    def __str__(self):
        return "Dealer has made " + str(self.netCash)

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

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
    def insurance(dealer, player):
        """Return Dealer, Player, True if player continues, False if player does not continue"""
        player_hand_value = Dealer.value_hand(player.get_hand())
        if dealer.get_hand()[0].get_value() == 11:
            if player_hand_value == 21:
                command = raw_input("The dealer is showing an Ace. Would you like take even money? y = Yes or n = No")
                while command != 'y' or command != 'Y' or command != 'n' or command != 'N':
                    if command == 'y' or command == 'Y':
                        player.set_current_bal_difference(player.get_current_bet())
                        return dealer, player, False
                    elif command == 'n' or command == 'N':
                        return dealer, player, True
                    else:
                        command = raw_input(
                            "Please type in a valid command. y = Yes or n = No")
            else:
                """Ask for insurance"""
                command = raw_input("The dealer is showing an Ace. Would you like get insurance? y = Yes or n = No")
                while command != 'y' or command != 'Y' or command != 'n' or command != 'N':
                    # TODO: Can make this into simpler statement
                    if command == 'y' or command == 'Y':
                        if dealer.get_hand()[1].get_value() == 10:
                            """Dealer has blackjack but player keeps even money"""
                            return dealer, player, False
                        else:
                            player.set_current_bal_difference(-player.get_current_bet()/2)
                            return dealer, player, True
                    elif command == 'n' or command == 'N':
                        if dealer.get_hand()[1].get_value() == 10:
                            """Dealer has blackjack but player loses money"""
                            player.set_current_bal_difference(-player.get_current_bet())
                            return dealer, player, False
                        else:
                            return dealer, player, True
                    else:
                        command = raw_input(
                            "Please type in a valid command. y = Yes or n = No")
        return dealer, player, True

    def dealer_play(self, dealer, player):
        """Returns the dealers hand after the moves. The strategy
        used can be found in Dealer Strategy.py"""
        command = ''
        print "Dealer Flipping card over"
        time.sleep(2)
        dealer_hand_value = Dealer.value_hand(self.hand)
        self.show_hand(self.hand, player.get_hand(), True)
        while command != 's' and dealer_hand_value < 21:
            command = self.dealer_move(self.hand)
            if command == 'h':
                dealt_card = self.deal_card()
                self.hand.append(dealt_card)
                time.sleep(2)
                self.show_hand(self.hand, player.get_hand(), True)
            dealer_hand_value = self.value_hand(self.hand)
        if dealer_hand_value > 21:
            print "\nDealer Busted! Total value is " + str(dealer_hand_value)
        return dealer, player

    @staticmethod
    def dealer_move(hand):
        return move(hand)

    @staticmethod
    def show_hand(dealer, player, show_card):
        """Prints out the current hand for User and Dealer."""
        print "-------------------------------"
        print "Dealer's Hand: "
        if show_card:
            for card in dealer:
                print card
        else:
            """The Dealer shows the hidden card when all players have gone."""
            print dealer[0]
            print "  -Hidden-"
        print "\nYour Hand:"
        for card in player:
            print card
        print "-------------------------------"

    @staticmethod
    def value_hand(hand):
        value = 0
        aces = 0
        for card in hand:
            """If Ace, skip over and calculate later """
            if card.get_value() == 11:
                aces += 1
            else:
                value += card.get_value()
        for i in range(0, aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value
