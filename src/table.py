import json
from src.card import Card
from src.row import Row

class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]
        
    def __repr__(self):
        repri = []
        for i, row in enumerate(self.rows):
            repri.append(f"r{i + 1}: {repr(row)}")
        return "\n".join(repri)


    def add_card(self, card: Card) -> bool:
        rowi = [row for row in self.rows if row.can_play(card)]

        if not rowi:
            return False

        # Сначала ищем пустую строку
        for row in rowi:
            if not row.cards: # Проверяем, пуста ли строка
                row.add_card(card)
                return True

        # Если пустых строк нет, выбираем строку с минимальной разницей
        rowm = min(rowi, key=lambda r: abs(card.num - r.cards[-1].num))
        rowm.add_card(card)
        return True

    def __getitem__(self, item):
        return self.rows[item]
    
    def save(self) -> str:
        return json.dumps({f"row{i + 1}": self.rows[i].save() for i in range(len(self.rows))})
    
    @classmethod
    def load(cls, rowstr: dict):
        table = cls()
        for rowkey, cardstr in rowstr.items():
            table.rows[int(rowkey[-1])-1] = Row.load(cardstr)
        return table