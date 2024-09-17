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
def test_eq():
    c1 = Card(30, 3)
    c2 = Card(30, 3)
    c3 = Card(20, 3)
    c4 = Card(10, 3)
    c5 = Card(55, 1)

    assert c1 == c2
    assert c1 != c3
    assert c1 != c4
    assert c1 != c5
def test_play_on():
    c1 = Card.load('10|3')
    c2 = Card.load('20|3')
    c3 = Card.load('30|3')
    c4 = Card.load('40|3')

    assert c1.can_play_on(c1)
    assert c2.can_play_on(c1)
    assert c1.can_play_on(c2)
    assert c3.can_play_on(c1)
    assert c4.can_play_on(c1)