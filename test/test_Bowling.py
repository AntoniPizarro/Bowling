from src.Strike import Strike
from src.Spare import Spare
from src.Gutterball import Gutterball
from src.BowlingPins import BowlingPins
from src.Roll import Roll
from src.Turn import Turn
import pytest

def test_Strike():
    assert Strike.addScore() == 10

def test_Spare():
    assert Spare.addScore() == 10

def test_Gutterball():
    assert Gutterball.addScore() == 0

def test_BowlingPins():
    assert BowlingPins(4).addScore() == 4
    assert BowlingPins(5).addScore() == 5
    assert BowlingPins(2).addScore() == 2
    assert BowlingPins(9).addScore() == 9
    assert BowlingPins(1).addScore() == 1
    assert BowlingPins(3).addScore() == 3
    
def test_Roll():
    assert Roll(5).getScore() == 5
    assert Roll(10).getScore() == 10
    assert Roll(6).getScore() == 6
    assert Roll(0).getScore() == 0

    assert Roll(BowlingPins(5).addScore()).getScore() == 5
    assert Roll(Strike.addScore()).getScore() == 10
    assert Roll(BowlingPins(6).addScore()).getScore() == 6
    assert Roll(Gutterball.addScore()).getScore() == 0

def test_Turn_Concluded():
    #assert Turn(turn_score, rolls, strike, last_turn).concluded()
    assert Turn(0, 2, False, False).concluded() == True
    assert Turn(0, 2, False, False).concluded() == True
    assert Turn(3, 2, False, False).concluded() == True
    assert Turn(0, 1, False, False).concluded() == False
    assert Turn(10, 1, True, False).concluded() == True
    assert Turn(7, 3, False, True).concluded() == True
    assert Turn(7, 2, False, True).concluded() == False

def test_Turn_GetScore():
    assert Turn(0, 1, False, False).addScore(10) == 10
    assert Turn(0, 1, False, False).addScore(0) == 0
    assert Turn(0, 1, False, False).addScore(6) == 6
    assert Turn(4, 2, False, False).addScore(6) == 10
    assert Turn(8, 2, False, False).addScore(0) == 8
    assert Turn(1, 2, False, False).addScore(6) == 7
    assert Turn(1, 3, False, True).addScore(6) == 7
    assert Turn(1, 2, False, True).addScore(6) == 7

    assert Turn(0, 1, False, False).addScore(Roll(Strike().addScore()).getScore()) == 10
    assert Turn(0, 1, False, False).addScore(Roll(Gutterball().addScore()).getScore()) == 0
    assert Turn(0, 1, False, False).addScore(Roll(BowlingPins(6).addScore()).getScore()) == 6
