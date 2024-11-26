from card import Card
from hand import Hand
from table import Table

from player_interaction import PlayerInteraction

class Human(PlayerInteraction):
    @classmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        """Выбор карты игроком и ввод"""
        while True:
            try:
                print('Карты в руке: ', hand)
                card_text = int(input('Выберите карту (введите номер карты): '))
                for card in hand.cards:
                    if card.num == card_text:
                        return card
                else:
                    print('Этой карты нет в руке')
            except ValueError as e:
                print(f"Ошибка: {e}")
    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Выбор ряда игроком и ввод"""
        while True:
            try:
                row_index = int(input("Выберите ряд, который заберете (1-4): ")) -1
                if not 0 <= row_index < len(table.rows):
                    raise ValueError(f"Неверный номер ряда.  Допустимые номера: 1-{len(table.rows)}")
                print(f"\tВыбрал ряд {row_index + 1}")
                return row_index
            except ValueError as e:
                print(f"Ошибка: {e}")