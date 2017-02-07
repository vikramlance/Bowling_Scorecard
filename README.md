# Bowling Scorecard
Python application for showing real time score card 

The application consists of 3 python scripts. The main script (BowlingGameMain.py) will take input as different scores of each throw of ball in bowling. The score will be displayed after each throw. Unit test case script test various scenarios.  

Rules of bowling scoring are http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm.

## Design and Development

Designing a single game 

Bowling-Scoring Basics 
One game of bowling consists of 10 frames, with a minimum score of zero and a maximum of 300. Each frame consists of two chances to knock down ten pins.
Input – series of 10 frames, each containing 2 throws (integers between 0 - 10), and 10th frame may contain 2 or 3 throws depending upon the outcome of first or second throw.
Output - score for each frame.

The basic entities of the bowling score dashboard are as follows
BolwingGame	-->	Frame	-->	Throw

Bowling game have one to many relationship with frame (1 game --> 10 frames), also frame have one to (1 .. many) relationship with throws. One frame will have 1,2,3 throws depending upon various situations.

I choose python to develop the code as it give lot of flexibility in programming.
Development is done according to test driven development (TDD) approach, where requirements are written as small test cases and code was developed according to test cases. Object oriented programming principles were followed to get modularized and maintainable code.

Basic structure of the program consists of bowlingGame.py which calculates the scores based on input given. It contains BowlingGame class which takes input as sores of a game and returns score, number of strikes, number of spares, and number of frames. 
For testing the code, I used pythons unit test framework which is very useful for running all the unit test cases.  Test cases validated various requirements for the scoreboard and can be found in BowlingScoreUnitTest.py

I wrote another wrapper program InteractiveBowlingGame.py to make an interactive bowling game scoreboard.  If this program is executed, it will ask inputs in the form of value of throws like integers from 0-9 , ‘x’ for strike (or 10), ‘/’ for spare.  After each entry It will provide score till that stage. In case it is not possible to calculate score for last frame then then it will output old scores which are available.

Caution: Code is developed in python 2.7 so some features might not work in python 3.x versions.

