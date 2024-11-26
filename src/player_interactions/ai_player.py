import random

from card import Card
from hand import Hand
from player import Player
from table import Table

from player_interaction import PlayerInteraction

class Bot(PlayerInteraction):
    @classmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        """Выбор карты ботом и ввод"""
        chosen_card = random.choice(hand.cards)
        return chosen_card
    
    @classmethod
    def choose_row(cls, table: Table, player: Player) -> int:
        numberrow = random.randint(0, len(table.rows) - 1)
        print(f"{player.name}({player.score}) забирает ряд {numberrow + 1}")
        return numberrow
    
    @classmethod
    def inform_card_chosen(cls, player: Player):
        """игрок выбрал карту."""
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """игрок выбрал ряд."""
        pass