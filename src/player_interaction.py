from abc import ABC, abstractmethod
from card import Card
from hand import Hand
from table import Table
from player import Player


class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        pass

    @classmethod
    @abstractmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        pass

    @classmethod
    def inform_card_chosen(cls, player: Player):
        """игрок выбрал карту."""
        pass

    @classmethod
    def inform_card_played(cls, card: Card):
        """карта использовалась."""
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """игрок выбрал ряд."""
        pass
