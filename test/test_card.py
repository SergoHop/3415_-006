import pytest

from src.card import Card

def test_init():
    c = Card(30)
    assert c.num == 30
    
def test_save():
    c = Card(30)
    assert repr(c) == '30'
    assert c.save() == '30'

    c = Card(55)
    assert repr(c) == '55'
    assert c.save() == '55'

def test_repr():
    c = Card(55)
    assert c.__repr__() == '55'
    assert Card.__repr__(Card(30)) == '30'

def test_load():
    s = '30'
    c = Card.load(s)
    assert c == Card(30)
    s = '55'
    c = Card.load(s)
    assert c == Card(55)
def test_eq():
    c1 = Card(30)
    c2 = Card(30)
    c3 = Card(20)
    c4 = Card(10)
    c5 = Card(55)

    assert c1 == c2
    assert c1 != c3
    assert c1 != c4
    assert c1 != c5
def test_play_on():
    c1 = Card.load('10')
    c2 = Card.load('20')
    c3 = Card.load('30')
    c4 = Card.load('40')

    assert not c1.can_play_on(c1)
    assert c2.can_play_on(c1)
    assert c3.can_play_on(c1)
    assert c4.can_play_on(c1)

def test_score():
    c = Card(70)
    assert 3 == c.score()
    c = Card(55)
    assert 7 == c.score()
    c = Card(11)
    assert 5 == c.score()

