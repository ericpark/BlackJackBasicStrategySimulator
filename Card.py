__author__ = 'ericpark'


class Card(object):
    """Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '  %s of %s' % (Card.rank_names[self.rank],
                               Card.suit_names[self.suit])

    def get_value(self):
        if Card.rank_names[self.rank] == "Ace":
            return 11
        elif Card.rank_names[self.rank] == "10" or \
                Card.rank_names[self.rank] == "Jack" or\
                Card.rank_names[self.rank] == "Queen" or \
                Card.rank_names[self.rank] == "King":
            return 10
        else:
            return int(Card.rank_names[self.rank])


