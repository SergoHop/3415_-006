from src.card import Card

class Row:

    mx = 6

    def __init__(self):
        self.cards: list[Card] = []

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
        if not self.cards:
            self.cards.append(card)
            return True
        else:
            if card.can_play_on(self.cards[-1]):
                self.cards.append(card)
                return True
            return False
        
        
                

            
    
