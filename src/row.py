from card import Card

class Row:

    mx = 6

    def __init__(self):
        self.cards: list[Card] = []

    def __eq__(self, other):
        return self.cards == other.cards
    
    def __str__(self):
        return ' '.join(repr(card)+f"({card.score()})" for card in self.cards)

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)

    def add_card(self, card: Card):
        return self.cards.append(card)

    def has_max_lengh(self) -> bool:
        return len(self.cards) == self.mx

    def truncate(self) -> int:#очистка
        summa = sum(c.score() for c in self.cards)
        self.cards.clear()
        return summa

    def can_play(self, card: Card) -> bool:
        return not self.cards or card.can_play_on(self.cards[-1])
        
    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)
    
    @staticmethod
    def load(data: str) -> 'Row':
        row = Row()
        spcards = data.split(' ')
        for card in spcards:
            row.add_card(Card.load(card))
        return row
                

            
    
