import unittest
import logging
from bowlingGame import BowlingGame, IncorrectThrow

from BowlingGameMain import 
       
     
class validGameScores(unittest.TestCase):
    
    def test_score_for_first_frame(self):
        pinsKnocked='54'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 9)
        self.assertEqual(totalStrikes, 0)
        self.assertEqual(totalSpares, 0)
        self.assertEqual(frame, 1)

    def test_score_for_three_frames_with_strike(self):
        pinsKnocked='54x34'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 33)
        self.assertEqual(totalStrikes, 1)
        self.assertEqual(totalSpares, 0)
        self.assertEqual(frame, 3)        
    
    def test_score_for_three_frames_with_spare(self):
        pinsKnocked='303/41'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 22)
        self.assertEqual(totalStrikes, 0)
        self.assertEqual(totalSpares, 1)
        self.assertEqual(frame, 3) 
    def test_score_for_seven_frames_with_strikes_and_spares(self):
        pinsKnocked='303/41xx2/34'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 84)
        self.assertEqual(totalStrikes, 2)
        self.assertEqual(totalSpares, 2)
        self.assertEqual(frame, 7)  

    def test_score_for_complete_game(self):
        pinsKnocked='x7/729/XXX236/7/3'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 168)

    def test_score_for_perfect_game(self):
        pinsKnocked='xxxxxxxxxxxx'
        newGame=BowlingGame(pinsKnocked)
        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
        self.assertEqual(score, 300)


if __name__ == '__main__':
    unittest.main()
