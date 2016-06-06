__author__ = 'ericpark'

from Dealer import Dealer
from Player import Player

"""Global Variables"""
table_min = 10
table_max = 500


def main():
    player = Player()
    dealer = Dealer()
    print "Hello! Welcome to Blackjack!"
    print "The table minimum is " + str(table_min)
    """Initialize variables"""
    hand_counter = 1
    while True:
        try:
            player.set_current_bal(int(raw_input("How much would you like to start with? \n")))
            break
        except ValueError:
            print "\nPlease type in a valid number.\n"
    while True:
        """Check if the player can play first."""
        if not player.get_current_bal() >= table_min:
            print "Sorry! You do not have enough money. Thank you for playing. "
            print "Your current balance is $" + str(p.get_current_bal())
            break

        """Get command (Check Balance, Leave Table, Next hand)"""
        print "\nCommands:"
        command = raw_input("Current balance is $" + str(
            player.get_current_bal()) + "   x = Exit   Enter in bet amount:\n(Or Enter to keep the previous bet.)\n")
        while command != 'x' or command != 'X':
            if command == '':
                print(player.get_current_bal())
                if player.get_current_bet() < table_min:
                    print "You have not put in an initial bet. " \
                          "Please bet above the table minimum: $" + str(table_min) + "\n"
                else:
                    break
            if command == 'x' or command == 'X':
                break
            else:
                try:
                    if table_min <= int(command) <= player.get_current_bal() and int(command) <= table_max:
                        player.set_current_bet(int(command))
                        break
                    else:
                        print "Please bet below your balance and within the table range: " \
                              "$" + str(table_min) + "-$" + str(table_max) + "\n"
                except ValueError:
                    print "\nPlease type in a valid command or " +\
                          "number above the table minimum ($" + str(table_min) + ")\n"
            command = raw_input("Current balance is $" + str(
                player.get_current_bal()) + "   x = Exit   Enter in bet amount:\n(Or Enter to keep the previous bet.)\n")

        if command == 'x':  # Exit the game
            break  # I know there is a better way to do this but this works.

        """Deal Hands"""
        print "\nHand " + str(hand_counter)
        player.set_hand(dealer.deal_hand())
        dealer.set_hand(dealer.deal_hand())

        dealer.show_hand(dealer.get_hand(), player.get_hand(), False)
        dealer, player, continue_game = dealer.insurance(dealer, player)

        if continue_game:
            """play"""
            dealer, player, bust = player.play(dealer, player)
            if not bust:
                print "Dealer wins."
            else:
                dealer, player = dealer.dealer_play(dealer, player)
        else:
            dealer.show_hand(dealer.get_hand(), player.get_hand(), True)
            if Dealer.value_hand(dealer.get_hand()) == 21:
                print "Dealer Wins. Dealer Hand Value: 21"

        hand_counter += 1
main()
