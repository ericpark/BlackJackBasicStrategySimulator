__author__ = 'ericpark'
from Dealer import Dealer


class Player(object):

    hand = []
    starting_bal = 0
    current_bal = 0
    current_bet = -1
    ai = False

    def __init__(self):
        self.hand = []
        self.current_bal = 0
        self.starting_bal = 0
        self.current_bet = -1

    def __str__(self):
        return "Player has made " + str(self.current_bal - self.starting_bal)

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def set_current_bal(self, bal):
        self.current_bal = bal

    def set_current_bal_difference(self, bal):
        self.current_bal += bal

    def get_current_bal(self):
        return self.current_bal

    def set_current_bet(self, bet):
        self.current_bet = bet

    def get_current_bet(self):
        return self.current_bet

    @staticmethod
    def play(dealer, player):
        command = ''
        player_hand_value = Dealer.value_hand(player.get_hand())
        if player_hand_value == 21:
            return dealer, player, True
        while command != 's' and player_hand_value < 21:
            """User Decides move (Hit, Fold, Double Down, Surrender?, Split)"""
            command = raw_input("\nh = Hit    f = Fold    s = Stay    sl = split    d = Double Down\n\n")

            if command == 'h':
                dealt_card = dealer.deal_card()
                hand = player.get_hand()
                hand.append(dealt_card)
                player.set_hand(hand)
                Dealer.show_hand(dealer.get_hand(), player.get_hand(), False)
            elif command == 'sl':
                """If splits are Ace, then only allow one card each."""
            elif command == 'd':
                dealt_card = dealer.deal_card()
                hand = player.get_hand()
                hand.append(dealt_card)
                player.set_hand(hand)
                Dealer.show_hand(dealer.get_hand(), player.get_hand(), False)
                player.set_current_bet(player.get_current_bet()*2)
                break
            player_hand_value = Dealer.value_hand(player.get_hand())

        if player_hand_value > 21:
            print "\nYou Busted. Total value is " + str(player_hand_value)
            return dealer, player, False
        return dealer, player, True
