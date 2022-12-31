import copy
import random
from typing import List

from mission_impossible.equipment import Card


class Pile:
    """Mission Impossible Game pile."""

    def __init__(self, card):
        self.card = card
        self.active = True

    def __repr__(self):
        return f"{self.card.value} {self.card.suit}" if self.active else "INACTIVE"

    def set_card(self, card: Card):
        self.card = card

    def destroy(self):
        self.active = False


class MissionImpossible:
    """
    Mission Impossible is a card game that works as follows:

    1. Take of deck of cards and draw n_piles (typically 9) cards and lay them face up.
    2. Guess whether the next card in the deck will be higher, lower, or equal to one of the face up cards.
    3. If your guess is correct, replace the face up card with the newly drawn card.
    4. If your guess is wrong, flip the pile over. It is now "destroyed".
    5. The game continues until all piles are flipped over (a loss) or all cards in the deck are drawn (a win).
    """

    def __init__(self, deck: List[Card], n_piles: int):
        self.deck = copy.deepcopy(deck)
        self.piles = {i: Pile(card=self.draw_card()) for i in range(n_piles)}

    def draw_card(self):
        """Draw one card randomly and remove it from the deck."""
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def guess(self, pile: Pile, direction: str):
        """Make a guess."""
        card = self.draw_card()
        if direction == "higher":
            if card > pile.card:
                pile.set_card(card)
            else:
                pile.destroy()
        elif direction == "lower":
            if card < pile.card:
                pile.set_card(card)
            else:
                pile.destroy()
        elif direction == "push":
            if card == pile.card:
                pile.set_card(card)
            else:
                pile.destroy()
        else:
            raise ValueError("Please enter a valid guess direction.")
        return card

    def check_game_continues(self):
        """Check to see if game is over."""
        if (
            len(self.deck) == 0
            or sum([pile.active for _, pile in self.piles.items()]) == 0
        ):
            return False
        else:
            return True

    def check_win_or_lose(self):
        """Check to see if we won or lost."""
        n_active_piles = sum([pile.active for _, pile in self.piles.items()])
        if len(self.deck) == 0 and n_active_piles > 0:
            return 1
        elif n_active_piles == 0:
            return 0
