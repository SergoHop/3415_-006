"""Карты для корова006."""
from typing import Self


class Card:
    
    NUMBERS = list(range(1,105))
    
    def __init__(self, num: int):
        if num not in Card.NUMBERS:
            raise ValueError
        self.num = num

    def __repr__(self):
        return f'{self.num}'
    
    def save(self):
        return repr(self)
    
    def __eq__(self, other):
        return self.num == other.num

    def load(text: str):
        """From 3 to Card(30, 3)."""
        return Card(num=int(text))
    
    def can_play_on(self, other: Self) -> bool:
        """Можно ли играть карту self на карту other."""
        return self.num < other.num
    def score(self) -> int:
        if self.num == 55:
            return 7
        elif self.num % 11 == 0:
            return 5
        elif self.num % 10 == 0:
            return 3
        elif self.num % 5 == 0:
            return 2
        else:
            return 1
