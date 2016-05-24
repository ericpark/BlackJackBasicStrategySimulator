__author__ = 'ericpark'

import DealerStrategy
from Dealer import Dealer
import Player

def main():
    print "Hello! Welcome to Blackjack!"
    continueGame = True
    handCounter = 1

    d = Dealer()
    print d
    #TODO: check for valid values.

    currentBal = int(raw_input("How much would you like to start with?"))

    while continueGame:
        print "Hand " + str(handCounter)

        #Get command (Check Balance, Leave Table, Next hand)
        #TODO: case sensitive
        command = raw_input("c = Check Balance \nn = Next hand \nx = Exit \n\n")
        while(command != 'x'):
            if command == 'c':
                print "Your current balance is $" + str(currentBal)
            if command == 'n':
                break
            else:
                print "Invalid Command."
            command = raw_input("c = Check Balance \nn = Nexthand \nx = Exit \n\n")

        if(command == 'x'):
            continueGame = False
            break

        #Deal Hand
        d.dealHand()

        #While user Turn:
        command = ''
        while(command != 's'): #TODO: Add in Bust function
            #User Decides move (Hit, Fold, Double Down, Surrender?, Split)
            command = raw_input("h = Hit \nf = Fold \ns = Stay \nsl = split \n\n")

        #Dealer Plays

        #Winner is paid out

        #if Dealer wins, subtract from current Balance

        #if Dealer loses, add to current Balance
        handCounter += 1

main()