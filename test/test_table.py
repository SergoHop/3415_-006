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
    
    