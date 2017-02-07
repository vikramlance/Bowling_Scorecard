from bowlingGame import BowlingGame, IncorrectThrow


throwScore1 =''
throwScore2 =''
cumulativeThrowScoreString =''

for i in range(1,11):
    if i <10 :
        throwScore1 = raw_input()
        
        if throwScore1=='x' :
            print i
            if len(cumulativeThrowScoreString) < 2:
                cumulativeThrowScoreString+= 'x'
                continue
            else:
                cumulativeThrowScoreString+= 'x'
                pinsKnocked=cumulativeThrowScoreString
                newGame=BowlingGame(pinsKnocked)
                score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
                print score
                
                continue
            else:
                throwScore2 = raw_input()
                if throwScore2 =='x':
                    if len(cumulativeThrowScoreString) < 2:
                        cumulativeThrowScoreString+= 'x'
                        continue
                    else:
                        cumulativeThrowScoreString+= 'x'
                        pinsKnocked=cumulativeThrowScoreString
                        newGame=BowlingGame(pinsKnocked)
                        score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
                        print score
                        
                        continue
            
        elif throwScore1 =='/':
            print "Invalid throw score"
        else:
            throwScore2 = raw_input()
            if throwScore2=='/':
                pinsKnocked=cumulativeThrowScoreString
                newGame=BowlingGame(pinsKnocked)
                score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
                print score
                cumulativeThrowScoreString+= throwScore1 + throwScore2
            else:
                cumulativeThrowScoreString+= throwScore1 + throwScore2
                pinsKnocked=cumulativeThrowScoreString
                newGame=BowlingGame(pinsKnocked)
                score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
                print score
    else:
        throwScore1 = raw_input()
        throwScore2 = raw_input()
        if throwScore1=='x' or throwScore2=='/':
            throwScore3 = raw_input()
            cumulativeThrowScoreString= cumulativeThrowScoreString + throwScore1 + throwScore2 + throwScore3
            pinsKnocked=cumulativeThrowScoreString
            newGame=BowlingGame(pinsKnocked)
            score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
            print score
        elif throwScore1=='0' and throwScore2=='x':
            throwScore3 = raw_input()
            throwScore4 = raw_input()
            cumulativeThrowScoreString= cumulativeThrowScoreString + throwScore2 + throwScore3 + throwScore4
            pinsKnocked=cumulativeThrowScoreString
            newGame=BowlingGame(pinsKnocked)
            score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
            print score            
        else:
            cumulativeThrowScoreString= cumulativeThrowScoreString + throwScore1 + throwScore2
            pinsKnocked=cumulativeThrowScoreString
            newGame=BowlingGame(pinsKnocked)
            score,totalStrikes,totalSpares,frame=newGame.displayFinalScore()
            print score
            

