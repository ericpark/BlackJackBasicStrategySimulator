__author__ = 'ericpark'

from Dealer import Dealer
import time

"""Global Variables"""
d = Dealer()


def main():
    print "Hello! Welcome to Blackjack!"
    """Initialize variables"""
    hand_counter = 1

    #TODO: check for valid values.

    current_bal = int(raw_input("How much would you like to start with? \n"))
    while True:
        """Get command (Check Balance, Leave Table, Next hand)"""
        #TODO: case sensitive
        command = raw_input("\nc = Check Balance    n = Nexthand    x = Exit \n")
        while command != 'x':
            if command == 'c':
                print "Your current balance is $" + str(current_bal)
            if command == 'n':
                break
            else:
                print "Invalid Command."
            command = raw_input("\nc = Check Balance    n = Nexthand    x = Exit \n")

        if command == 'x':
            break

        print "\nHand " + str(hand_counter)

        """Deal Hands"""
        hand = d.deal_hand()
        dealer = d.deal_hand()
        show_hand(hand, dealer, False)

        """While user's turn:"""
        hand = play(hand, dealer)

        if value_hand(hand) <= 21:
            """Dealer plays if user did not bust"""
            print "Dealer Flipping card over"
            time.sleep(1)
            show_hand(hand, dealer, True)
            dealer = dealer_play(hand, dealer)
            if value_hand(hand) > value_hand(dealer) or value_hand(dealer) > 21:
                print "You win!"
            elif value_hand(hand) == value_hand(dealer):
                print "Push! Tie"
            else:
                print "Dealer wins."
        else:
            print "Dealer wins."
        hand_counter += 1


def play(hand, dealer):
    command = ''
    hand_value = value_hand(hand)
    while command != 's' and hand_value < 21:
        """User Decides move (Hit, Fold, Double Down, Surrender?, Split)"""
        command = raw_input("\nh = Hit    f = Fold    s = Stay    sl = split \n\n")
        if command == 'h':
            hand.append(d.deal_card())
            show_hand(hand, dealer, False)
        hand_value = value_hand(hand)

    if hand_value > 21:
        print "\nYou Busted. Total value is " + str(hand_value)
    return hand


def dealer_play(hand, dealer):
    """Returns the dealers hand after the moves. The strategy
    used can be found in Dealer Strategy.py"""
    command = ''
    hand_value = value_hand(dealer)
    while command != 's' and hand_value < 21:
        command = d.dealer_move(dealer)
        if command == 'h':
            dealer.append(d.deal_card())
            time.sleep(2)
            show_hand(hand, dealer, True)
        hand_value = value_hand(dealer)
    if hand_value > 21:
        print "\nDealer Busted! Total value is " + str(hand_value)
    return dealer


def value_hand(hand):
    """Returns the total value of the hand. """
    value = 0
    aces = 0
    for card in hand:
        """if Ace, skip over and calculate later"""
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


def show_hand(hand, dealer, show_card):
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
    for card in hand:
        print card
    print "-------------------------------"
main()
