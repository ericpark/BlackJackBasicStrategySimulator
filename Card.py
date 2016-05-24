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
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def getValue(self):
        if self.rank == "Ace":
            return 11
        elif self.rank == "10" or self.rank == "Jack" or self.rank == "Queen" or self.rank == "King":
            return 10
        else:
            return int(self.rank)


