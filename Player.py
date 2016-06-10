__author__ = 'ericpark'
from Dealer import Dealer
import time


class Player(object):

    hand = []
    hands = []
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

    def get_hand(self):
        return self.hand

    def get_hands(self):
        return self.hands

    def get_current_bal(self):
        return self.current_bal

    def get_current_bet(self):
        return self.current_bet

    def set_hand(self, hand):
        self.hand = hand

    def set_hands(self, hands):
        self.hands = hands

    def set_current_bal(self, bal):
        self.current_bal = bal

    def set_current_bet(self, bet):
        self.current_bet = bet

    def set_current_bal_difference(self, bal):
        self.current_bal += bal

    @staticmethod
    def play(dealer, player, can_split_again):
        player.set_hands([])
        command = ''
        player_hand_value = Dealer.value_hand(player.get_hand())
        turn = 1
        if player_hand_value == 21:
            player.set_hands([player.get_hand()])
            return dealer, player, True
        while command != 's' and player_hand_value < 21:
            """User Decides move (Hit, Fold, Double Down, Surrender?, Split)"""
            command = raw_input("\nh = Hit    su = Surrender    s = Stay    sl = split    d = Double Down\n\n")

            if command == 'h':
                dealt_card = dealer.deal_card()
                hand = player.get_hand()
                hand.append(dealt_card)
                player.set_hand(hand)
                Dealer.show_hand(dealer.get_hand(), player.get_hand(), False)
                turn += 1
            elif command == 'sl':
                """If splits are Ace, then only allow one card each."""
                hand = player.get_hand()
                hands = player.get_hands()
                if hand[0].get_value() == hand[1].get_value():
                    if turn == 1 and can_split_again:
                        print "Splitting " + str(hand[1].get_value()) + "'s"
                        if hand[0].get_value() == 11:
                            print "Aces are only split once"
                            for i in range(0, 2):
                                dealt_card = dealer.deal_card()
                                new_hand = [hand[0], dealt_card]
                                hands.append(new_hand)
                            player.set_hands(hands)
                            Dealer.show_hand(dealer.get_hand(), player.get_hands(), False)
                            return dealer, player, True
                        else:
                            total_hands = []
                            for i in range(0, 2):
                                dealt_card = dealer.deal_card()
                                new_hand = [hand[i], dealt_card]
                                hands.append(new_hand)
                            player.set_hands(hands)
                            Dealer.show_hand(dealer.get_hand(), player.get_hands(), False)
                            print "Playing Each hand:"
                            not_bust = True
                            time.sleep(2)
                            for i in range(0, 2):
                                temp_p = Player()
                                temp_p.set_hand(hands[i])
                                Dealer.show_hand(dealer.get_hand(), temp_p.get_hand(), False)
                                dealer, temp_p, bust = Player.play(dealer, temp_p, True)
                                temp_p_hands = temp_p.get_hands()
                                for j in range(0, len(temp_p_hands)):
                                    total_hands.append(temp_p_hands[j])
                                not_bust = not_bust and bust
                            player.set_hands(total_hands)
                            return dealer, player, not_bust
                    else:
                        print "Sorry! You can only split on the first turn."
                else:
                    print "Sorry! Your cards have to the same."
                turn += 1
            elif command == 'd':
                if turn == 1:
                    dealt_card = dealer.deal_card()
                    hand = player.get_hand()
                    hand.append(dealt_card)
                    player.set_hand(hand)
                    Dealer.show_hand(dealer.get_hand(), player.get_hand(), False)
                    player.set_current_bet(player.get_current_bet()*2)
                    player_hand_value = Dealer.value_hand(player.get_hand())
                    player.set_hands([hand])
                    break
                else:
                    print "Sorry! Can only double down on the first turn!"
                turn += 1
            elif command == 'su':
                if turn == 1:
                    player.set_current_bal_difference(player.get_current_bet()/2)
                    print "You surrender!"
                    return dealer, player, False
                else:
                    print "Sorry! Can only surrender on the first turn!"
                turn += 1
            player_hand_value = Dealer.value_hand(player.get_hand())
        if player_hand_value > 21:
            print "\nYou Busted. Total value is " + str(player_hand_value)
            return dealer, player, False
        player.set_hands([player.get_hand()])
        return dealer, player, True

