__author__ = 'ericpark'

from Dealer import Dealer
import time

"""Global Variables"""
d = Dealer()
table_min = 10


def main():
    print "Hello! Welcome to Blackjack!"
    print "The table minimum is " + str(table_min)
    """Initialize variables"""
    hand_counter = 1
    while True:
        try:
            current_bal = int(raw_input("How much would you like to start with? \n"))
            break
        except ValueError:
            print "\nPlease type in a valid number.\n"
    current_bet = 0
    while True:
        """Get command (Check Balance, Leave Table, Next hand)"""
         #TODO: case sensitive

        if current_bal < table_min:
            print "Sorry! You do not have enough money. Thank you for playing. "
            print "Your current balance is $" + str(current_bal)
            break

        print "\nCommands:"
        command = raw_input("Current balance is $" + str(
            current_bal) + "   x = Exit   Enter in bet amount:\n(Or Enter to keep the previous bet.)\n")
        while command != 'x':
            if command == 'x':
                break
            if command == '':
                if current_bet < table_min:
                    print "You have not put in an initial bet. " \
                          "Please bet above the table minimum: $" + str(table_min) + "\n"
                else:
                    break
            else:
                try:
                    if table_min <= int(command) <= current_bal:
                        current_bet = int(command)
                        break
                    else:
                        print "Please bet below your balance and above the table minimum: $" + str(table_min) + "\n"
                except ValueError:
                    print "\nPlease type in a valid command or " +\
                          "number above the table minimum ($" + str(table_min) + ")\n"
            command = raw_input("Current balance is $" + str(
                current_bal) + "   x = Exit   Enter in bet amount:\n(Or Enter to keep the previous bet.)\n")

        if command == 'x':
            break

        print "\nHand " + str(hand_counter)

        """Deal Hands"""
        hand = d.deal_hand()
        dealer = d.deal_hand()
        show_hand(hand, dealer, False)

        """While user's turn:"""
        hand = play(hand, dealer)
        hand_value = value_hand(hand)
        if hand_value == 21 and len(hand) == 2:
            """Player got blackjack"""
            current_bal += current_bet * 1.5
            print "Blackjack!"
        elif value_hand(hand) <= 21:
            """Dealer plays if user did not bust"""
            print "Dealer Flipping card over"
            time.sleep(1)
            show_hand(hand, dealer, True)
            dealer = dealer_play(hand, dealer)
            if value_hand(hand) > value_hand(dealer) or value_hand(dealer) > 21:
                current_bal += current_bet
                print "You win!"
            elif value_hand(hand) == value_hand(dealer):
                print "Push! Tie"
            else:
                current_bal -= current_bet
                print "Dealer wins."
        else:
            print "Dealer wins."
        hand_counter += 1


def play(hand, dealer):
    command = ''
    hand_value = value_hand(hand)
    if hand_value == 21:
        return hand
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
