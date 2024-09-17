import pytest

from src.card import Card

def test_init():
    c = Card(30, 3)
    assert c.num == 30
    assert c.shtraf == 3
def test_save():
    c = Card(30, 3)
    assert repr(c) == '30|3'
    assert c.save() == '30|3'

    c = Card(55, 7)
    assert repr(c) == '55|7'
    assert c.save() == '55|7'

def test_load():
    s = '30|3'
    c = Card.load(s)
    assert c == Card(30,3)
    s = '55|7'
    c = Card.load(s)
    assert c == Card(55,7)

