import json
from card import Card
from row import Row

class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]
        
    def __repr__(self):
        repri = []
        for i, row in enumerate(self.rows):
            repri.append(f"r{i + 1}: {repr(row)}")
        return "\n".join(repri)

    def __str__(self):
        str_rows = [f"row{i + 1}: {str(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(str_rows)


    def add_card(self, card: Card) -> bool: 
        good_rows = []#Список рядов, в которых номер карты меньше чем номер выбранной
        for row in self.rows:#Проверка, что номер выбранной больше
            if row.can_play(card):
                good_rows.append(row)
        if not good_rows:#Если ни один ряд не подходит
            return False
        
        best_row = min(good_rows, key=lambda r: abs(card.num - r.cards[-1].num))#Ряд с наименьшей разницей
        if len(best_row.cards) == Row.mx - 1:#Если карта шестая в ряду
            print(f'Игрок забрал ряд {self.rows.index(best_row) + 1}')
            best_row.truncate()

        best_row.add_card(card)#Шестая карта становится первой в ряду
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