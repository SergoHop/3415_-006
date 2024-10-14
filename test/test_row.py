from src.card import Card
from src.row import Row


def test_init():
    r = Row()
    assert r.__init__() == None

def test_repr():
    r = Row()
    assert r.__repr__() == ''
    r.add_card(Card(10))
    assert r.__repr__() == '10'

def test_add_card():
    r = Row()
    r.add_card(Card(10))
    r.add_card(Card(20))
    assert r.cards == [Card(10), Card(20)]
    assert r.cards != [Card(10)]
    assert r.cards != [Card(20)]
    r.add_card(Card(30))
    assert r.cards == [Card(10), Card(20), Card(30)]

def test_max_lengh():
    r = Row()
    r.add_card(Card(10))
    assert r.has_max_lengh() == False

    r.add_card(Card(20))
    assert r.has_max_lengh() == False

    r.add_card(Card(30))
    assert r.has_max_lengh() == False

    r.add_card(Card(40))
    assert r.has_max_lengh() == False

    r.add_card(Card(50))
    assert r.has_max_lengh() == False

    r.add_card(Card(55))
    assert r.has_max_lengh() == True

    r.add_card(Card(55))
    assert r.has_max_lengh() == False

def test_truncate():
    r = Row()
    r.add_card(Card(55))
    r.truncate()
    assert r.cards == []

def test_can_play_on():
    r = Row()
    assert r.can_play(Card(55)) == True

    r.add_card(Card(10))
    assert r.can_play(Card(3)) == False  
    assert r.can_play(Card(30)) == True 
