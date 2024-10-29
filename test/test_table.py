import json
from src.card import Card
from src.row import Row
from src.table import Table

def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    assert not len(table.rows) == 5
def test_repr():
    table = Table()

    table.add_card(Card(10))
    table.add_card(Card(20))
    table.add_card(Card(30))
    table.add_card(Card(40))
    table.add_card(Card(35))
    table.add_card(Card(45))

    reprtest = f"r1: {Card(10)}\nr2: {Card(20)}\nr3: {Card(30)} {Card(35)}\nr4: {Card(40)} {Card(45)}"
    assert repr(table) == reprtest
    reprtest = f"r1: {Card(10)}\nr2: {Card(20)}\nr3: {Card(30)} {Card(45)}\nr4: {Card(40)} {Card(35)}"
    assert not repr(table) == reprtest

def test_add_card():
    table = Table()
    table.add_card(Card(10))
    table.add_card(Card(20))
    table.add_card(Card(30))
    table.add_card(Card(40))
    table.add_card(Card(35))
    table.add_card(Card(45))
    
    assert repr(table[0]) == '10'
    assert repr(table[1]) == '20'
    assert repr(table[2]) == '30 35'
    assert repr(table[3]) == '40 45'
    assert not table.add_card(Card(5))

def test_save():
    table = Table()
    table.rows[0].add_card(Card(10))
    table.rows[1].add_card(Card(20))
    table.rows[2].add_card(Card(30))
    table.rows[3].add_card(Card(40))
    table.add_card(Card(15))
    table.add_card(Card(25))
    table.add_card(Card(35))
    table.add_card(Card(45))
    save_table = table.save()
    json_table = json.dumps({
        'row1': '10 15',
        'row2': '20 25',
        'row3': '30 35',
        'row4': '40 45'})
    assert save_table == json_table

def test_load():
    data = {
        'row1': '10 15',
        'row2': '20 25',
        'row3': '30 35',
        'row4': '40 45'}
    table = Table.load(data)
    assert table[0].cards[0] == Card(10)
    assert table[0].cards[1] == Card(15)
    assert table[1].cards[0] == Card(20)
    assert table[1].cards[1] == Card(25)
    assert table[2].cards[0] == Card(30)
    assert table[2].cards[1] == Card(35)
    assert table[3].cards[0] == Card(40)
    assert table[3].cards[1] == Card(45)
    assert len(table[0].cards) == 2
    assert len(table[1].cards) == 2
    assert len(table[2].cards) == 2
    assert len(table[3].cards) == 2
    assert not len(table[3].cards) == 3
    
    

    
    
    