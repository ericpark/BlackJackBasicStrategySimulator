__author__ = 'ericpark'

from Dealer import Dealer
from Player import Player
from Card import Card
import decimal

"""Global Variables"""
table_min = 10
table_max = 500


def main():
    player = Player()
    dealer = Dealer()
    print "Hello! Welcome to Blackjack!"
    print "The table minimum is " + str(table_min) + " and table maximum is " + str(table_max)
    """Initialize variables"""
    hand_counter = 1
    while True:
        try:
            player.set_current_bal(decimal.Decimal(raw_input("How much would you like to start with? \n")))
            break
        except decimal.InvalidOperation:
            print "\nPlease type in a valid number.\n"
    while True:
        """Check if the player can play first."""
        if not player.get_current_bal() >= table_min:
            print "Sorry! You do not have enough money. Thank you for playing. "
            print "Your current balance is $" + str(player.get_current_bal())
            break

        """Get command (Check Balance, Leave Table, Next hand)"""
        print "\nCommands:"
        command = raw_input("Current balance is $" + str(
            player.get_current_bal()) + "   x = Exit   Enter in bet amount:\n(Or Enter to keep the previous bet.)\n")
        while command != 'x' or command != 'X':
            if command == '':
                if player.get_current_bet() < table_min:
                    print "You have not put in an initial bet. " \
                          "Please bet above the table minimum: $" + str(table_min) + "\n"
                elif player.get_current_bet() > player.get_current_bal() or \
                        not table_min <= player.get_current_bet() <= table_max:
                    player.set_current_bet(0)
                    print "Please reenter your bet below your balance and within the table range: " \
                          "$" + str(table_min) + "-$" + str(table_max) + "\n"
                else:
                    break
            elif command == 'x' or command == 'X':
                break
            else:
                try:
                    if table_min <= decimal.Decimal(command) <= player.get_current_bal() and decimal.Decimal(command) <= table_max:
                        player.set_current_bet(decimal.Decimal(command))
                        break
                    else:
                        print "Please bet below your balance and within the table range: " \
                              "$" + str(table_min) + "-$" + str(table_max) + "\n"
                except decimal.InvalidOperation:
                    print "\nPlease type in a valid command or " +\
                          "number above the table minimum ($" + str(table_min) + ")\n"
            command = raw_input("Current balance is $" + str(
                player.get_current_bal()) + "   x = Exit   Enter in bet amount:\n"
                                            "(Or Enter to keep the previous bet.)\n")

        if command == 'x':  # Exit the game
            break  # I know there is a better way to do this but this works.

        """Deal Hands"""
        print "\nHand " + str(hand_counter)
        player.set_hand(dealer.deal_hand())
        dealer.set_hand(dealer.deal_hand())

        dealer.show_hand(dealer.get_hand(), [player.get_hand()], False)
        dealer, player, continue_game = dealer.insurance(dealer, player)

        if continue_game:
            """play"""
            dealer, player, bust = player.play(dealer, player, True)
            if not bust:
                player.set_current_bal_difference(-player.get_current_bet())
                print "Dealer wins."
            else:
                if len(player.get_hands()) == 1:
                    if len(player.get_hand()) == 2 and Dealer.value_hand(player.get_hand()) == 21:
                        player.set_current_bal_difference(decimal.Decimal(1.5) * player.get_current_bet())
                        print "Winner Winner Chicken Dinner! Blackjack! You win!"
                    else:
                        dealer, player = dealer.dealer_play(dealer, player)
                        dealer_hand = Dealer.value_hand(dealer.get_hand())
                        player_hand = Dealer.value_hand(player.get_hand())
                        if player_hand > dealer_hand or dealer_hand > 21:
                            player.set_current_bal_difference(player.get_current_bet())
                            print "You win!"
                        elif player_hand == dealer_hand:
                            print "Push! Tie"
                        else:
                            player.set_current_bal_difference(-player.get_current_bet())
                            print "Dealer wins."
                else:
                    dealer, player = dealer.dealer_play(dealer, player)
                    dealer_hand = Dealer.value_hand(dealer.get_hand())
                    split_hand = 1
                    for hand in player.get_hands():
                        player_hand = Dealer.value_hand(hand)
                        if player_hand > 21:
                            print "Hand " + str(split_hand) + " busts!"
                        elif player_hand > dealer_hand or dealer_hand > 21:
                            player.set_current_bal_difference(player.get_current_bet())
                            print "Hand " + str(split_hand) + " wins!"
                        elif player_hand == dealer_hand:
                            print "Hand " + str(split_hand) + " pushes! Tie"
                        else:
                            player.set_current_bal_difference(-player.get_current_bet())
                            print "Hand " + str(split_hand) + " Dealer wins"
                        split_hand += 1
        else:
            dealer.show_hand(dealer.get_hand(), player.get_hand(), True)
            if Dealer.value_hand(dealer.get_hand()) == 21 and Dealer.value_hand(player.get_hand()) == 21:
                print "Push! Tie"
            elif Dealer.value_hand(dealer.get_hand()) == 21:
                print "Dealer Wins. Dealer Hand Value: 21"
            else:
                print "Dealer Wins! ~ But not exactly sure why"

        hand_counter += 1
    print player
main()
