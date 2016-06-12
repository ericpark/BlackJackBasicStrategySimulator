__author__ = 'ericpark'


def move(dealer, player):
    value, soft = value_hand(dealer.get_hand())
    """Check if "soft" 17"""

    if value < 17:
        return "h"
    elif value == 17 and soft:
        return "h"
    else:
        return "s"


def value_hand(hand):
    value = 0
    aces = 0
    soft = False
    for card in hand:
        """If Ace, skip over and calculate later """
        if card.get_value() == 11:
            aces += 1
        else:
            value += card.get_value()
    for i in range(0, aces):
        if value + 11 <= 21:
            value += 11
            soft = True
        else:
            value += 1
    return value, soft
