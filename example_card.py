import dataclasses
import enum
import functools
import itertools
from typing import List


class Suit(enum.IntEnum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

    def __str__(self) -> str:
        return "♧♦♡♠"[int(self.value)]

    def __format__(self, _: str) -> str:
        return str(self)

    @property
    def name(self) -> str:  # type: ignore[override]
        return str(super().name).capitalize()


class Rank(enum.IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self) -> str:
        if self.value > 9:
            return self.name[0]
        return str(self.value)

    def __format__(self, _: str) -> str:
        return str(self)

    @property
    def name(self) -> str:  # type: ignore[override]
        return str(super().name).capitalize()


# The total_ordering ignores the trump suit; it's intended only for sorting the cards in a hand, for display.
@functools.total_ordering
@dataclasses.dataclass
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{self.suit}{self.rank}"

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def deck(kls) -> List['Card']:
        return list(kls(*p) for p in itertools.product(Suit, Rank))

    def __lt__(self, other: 'Card') -> bool:
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        return self.rank < other.rank
