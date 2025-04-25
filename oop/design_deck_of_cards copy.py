# Python 3

from abc import ABC, abstractmethod
from typing import List


class ICard(ABC):
    @abstractmethod
    def stringify(self) -> str:
        pass


class PokerCard(ICard):
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def stringify(self) -> str:
        return f"{self.value} of {self.suit}s"


class FlinchCard(ICard):
    def __init__(self, number: int):
        self.number = number

    def stringify(self) -> str:
        return str(self.number)


class Deck:
    def __init__(self):
        self.cards: List[ICard] = []

    def create(self, cards: List[ICard]) -> None:
        self.cards = list(cards)

    def take(self) -> ICard:
        return self.cards.pop()

    def look(self) -> str:
        return self.cards[-1].stringify()


if __name__ == "__main__":
    cards = [
        PokerCard("club", "three"),
        PokerCard("heart", "four")
    ]
    deck = Deck()
    deck.create(cards)
    print(deck.look())  # -> "four of hearts"
