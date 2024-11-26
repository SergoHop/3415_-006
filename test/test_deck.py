import random

from card import Card
from deck import Deck

cards = [Card(10), Card(20), Card(55)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards

def test_repr():
    
    d = Deck(cards)
    d1 = Deck([Card(30)])
    
    assert d.__repr__() == "10 20 55"
    assert d1.__repr__() == "30"
    assert Deck([Card(40)]).__repr__() == "40"

def test_eq():
     
    d = Deck(cards)
    d1 = Deck(cards)
    d2 = Deck([Card(10), Card(20), Card(55)])
    d3 = Deck([Card(30), Card(40)])
    
    assert d == d1
    assert d == d2
    assert d != d3

def test_save():
    
    d = Deck(cards=cards)
    assert d.save() == '10 20 55'

    d = Deck(cards=[])
    assert d.save() == ''

def test_load():
    
     
    d = Deck.load('10 20 55')
    expected_deck = Deck(cards)
    
    assert str(d) == str(expected_deck)
    assert d == expected_deck

def test_draw_card():
    d = Deck.load('10 12 55')
    d1 = Deck.load('10 12')

    assert d.draw_card() == Card.load('55')
    assert d == d1
    assert len(d.cards) == 2

    assert d.draw_card() == Card.load('12')
    assert d != d1
    assert len(d.cards) == 1

    assert d.draw_card() == Card.load('10')
    assert len(d.cards) == 0


def test_shuffle():
    random.seed(2)

    
    deck = Deck(cards=cards)

    deck.shuffle()
    assert deck.save() == '20 55 10'
    
    deck.shuffle()
    assert deck.save() == '10 55 20'
    
    
