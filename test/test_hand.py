import random

from src.card import Card
from src.hand import Hand

cards = [Card(10), Card(20), Card(55)]

def test_init():
    d = Hand(cards=cards)
    assert d.cards == cards

def test_repr():
    d = Hand(cards)
    d1 = Hand([Card(30)])

    assert d.__repr__() == '10 20 55'
    assert d1.__repr__() == '30'
    assert Hand([Card(3)]).__repr__() == '3'

def test_eq():
    h = Hand(cards)
    h2 = Hand([Card(30), Card(40), Card(50)])
    h3 = Hand([Card(40), Card(51)])

    assert h != h2
    assert h != h3

def test_save():
    d = Hand(cards=cards)
    assert d.save() == '10 20 55'

    d = Hand(cards=[])
    assert d.save() == ''

def test_load():
    d = Hand.load('10 20 55')
    expected_deck = Hand(cards)
    assert d == expected_deck

def test_add_card():
    h = Hand.load('10 20 55')
    h.add_card(Card.load('30'))
    assert repr(h) == '10 20 55 30'

def test_remove_card():
    h = Hand.load('10 20 55')
    c = Card.load('20')
    h.remove_card(c)
    assert repr(h) == '10 55'

def test_score():
    h = Hand.load('10 20 55')
    assert h.score() == 13
   

