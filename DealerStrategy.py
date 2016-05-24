__author__ = 'ericpark'

def move(cards):
    #Add up Cards
    sum = 0

    #Check if "soft" 17

    if(sum < 17):
        return "HIT"
    else:
        return "STAY"