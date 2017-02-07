'''
Bowling Game Scoreboard

This program contains two classes one for exception handling and other for calculating bowling score based on input given.

Input format = string containing outcomes of each throw in a bowling game , it can contain integers 0 to 9 , 'x' for strike and '/' for spare.

Special case - In a frame 0 and 'x' will be considered as '/' cause x is equivalent to 10 so it will be frame of (0,10)

The input string should contain valid throw scores , each frame should not exceed total of 10. The final frame in the game (10th frame) will
contain 2 or 3 throws depending upon the ouctome of first throw in the frame.
All the rules are followed from http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm

Output format = It will return  total score, total strikes,total spares, total frames
'''
class IncorrectThrow(Exception):
    pass

# Takes input of throws (number of pins knocked) and calculates score for the game.
class BowlingGame:
    def __init__(self,pinsKnocked=''):
        self.pinsKnocked = pinsKnocked
        
    # Checks if given string contains valid throw scores for a bowling game, input should only contain integers,'x', and '/'
    def validateInput(self,pinsKnocked):
        if (self.pinsKnocked!='') and (self.pinsKnocked !=None):
            removeStrike=pinsKnocked.replace('x','')
            removeSpare=removeStrike.replace('/','')
            try:
                int(removeSpare)
            except ValueError as e:
                message= ("One or more of the scores provided for throw is/are invalid")
                raise type(e)(message)
            else:
                return throwScores
    
    # Create array containing pins knocked in each throw with sequential frames.
    # When we get number of pins knocked in new throw then it will be appended in this array.
    def pinsKnockedArray(self):
        pinsArray = []
        previousThrow =None
        # Process all the outcomes of throws one by one and add it to an array
        for i in self.pinsKnocked:

            throwScore=self.throwValue(i,previousThrow)

            previousThrow= throwScore
            
            pinsArray.append(throwScore)
        return pinsArray
    
    # Convert strike and spare values into integer values 
    def throwValue(self,throw,previousThrow=None):
            
        if throw.upper()=='X':
            return 10
        elif throw == '/':
            return (10 - previousThrow)
        else:
            return int(throw)    

    #Process each frame score one by one and apply bowling rules to calculate the cumulative scores for given input
    def recursiveScore(self,numPins=[],frame=0,score=0):
        # If strike then add next two throw scores
        if (numPins[0]==10 ):
            if (len(numPins)>2):
                score+=sum(numPins[:3])
                # Remove frame score from the array once it is processed
                numPins=numPins[1:]
                
                # When last 2 frames are strike then show score without last 2 frame
                if ((numPins==[10,10]) or (frame ==10)):
                    numPins=[]
                # When value of strike can't be calculated then show score without it
                else:
                    if (len(numPins)< 2):
                        numPins=[]
        else:
            # Calculate sum of the throw scors in a frame
            frameSum=sum(numPins[:2])
            if frameSum<10:
                score+=frameSum
                # for spare calculate sum by adding next outcome of throw
            elif frameSum == 10:
                #When last frame is spare then show score without last frame
                if (len(numPins)==2):
                    numPins=[]
                elif frame==10:
                    score+=sum(numPins[:3])
                    numPins=[]
                else:
                    score+=sum(numPins[:3])
            else:
                raise IncorrectThrow("Invalid number of pins knocked ")
            # Remove frame score from the array once it is processed
            numPins=numPins[2:]
            if (len(numPins)==1 and numPins!=[10]):         # When frame is not complete then show score without last frame
                numPins=[]
            
        # Stop recursion when there are no more score or frame is 10     
        if ((frame == 10) or (not numPins) ):
            # Count total number of strikes and spares in the game
            totalStrikes= self.pinsKnocked.upper().count('X')
            totalSpares=self.pinsKnocked.count('/')
            return (score, totalStrikes,totalSpares, frame)
        return self.recursiveScore(numPins=numPins, frame=frame+1, score=score)
 
    def displayFinalScore(self):        
        return self.recursiveScore(numPins=self.pinsKnockedArray(),frame=1,score=0 )
