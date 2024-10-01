from src.hand import Hand
from src.player import Player

def test_init():
    h = Hand.load('10 20 55')
    p = Player(name='Sergo', hand=h, score=13)
    assert p.name == 'Sergo'
    assert p.hand == h
    assert p.score == 13

def test_str():
    h = Hand.load('10 20 55')
    p = Player(name='Sergo', hand=h, score=13)
    assert str(p) == 'Sergo(13): 10 20 55'

def test_loser():
    h = Hand.load('10 20 55')
    p = Player(name='Sergo', hand=h, score=13)
    assert not p.loser()

    p = Player(name='Sergo', hand=h, score=66)
    assert p.loser()

def test_eq():
    h1 = Hand.load('10 20 55')
    h2 = Hand.load('10 20 55')
    p1 = Player(name='Sergo', hand=h1, score=13)
    p2 = Player(name='Sergo', hand=h2, score=13)
    assert p1 == p2

def test_save():
    h = Hand.load('10 20 55')
    p = Player(name='Sergo', hand=h, score=13)
    assert p.save() == {'name': 'Sergo', 'score': 13, 'hand': '10 20 55'}

def test_load():
    data = {'name': 'Sergo', 'score': 13, 'hand': '10 20 55'}
    h = Hand.load('10 20 55')
    p_expected = Player(name='Sergo', hand=h, score=13)
    p = Player.load(data)
    assert p == p_expected

