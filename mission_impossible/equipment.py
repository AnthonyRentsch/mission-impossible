import copy

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
SUITS = ["spades", "clubs", "diamonds", "hearts"]


class Card:
    """Standard card."""

    values = copy.deepcopy(VALUES)
    suits = copy.deepcopy(SUITS)

    def __init__(self, value, suit):

        normalized_value = str(value).lower()
        normalized_suit = str(suit).lower()

        if normalized_value not in self.values:
            raise ValueError("Invalid card value.")
        else:
            self.value = normalized_value

        if normalized_suit not in self.suits:
            raise ValueError("Invalid card suit.")
        else:
            self.suit = normalized_suit

    def __repr__(self):
        return f"{self.value} {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.values.index(self.value) < self.values.index(other.value)

    def __gt__(self, other):
        return self.values.index(self.value) > self.values.index(other.value)
