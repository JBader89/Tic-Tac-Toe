# Jeremy Bader, Katie Ketcham
# Midterm Project
# An Optimal Strategy Playing Tic Tac Toe Computer
# Used as a starting point: http://en.literateprograms.org/Tic_Tac_Toe_(Python)?oldid=17009

import operator, sys, time, random
from graphics import *

def allEqual(list):
    """returns True if all the elements in a list are equal, or if the list is empty."""
    return not list or list == [list[0]] * len(list)

Empty = ' '
# user and computer will end up being X or O randomly 
User = 'x'
Computer = 'o'

class Board:
    """This class represents a tic tac toe board state."""
    
    def __init__(self):
        """Initialize all members."""
        
        # 9 empty spaces on the board, labeled as number 1-9
        self.pieces = [Empty]*9
            
    def winner(self):
        """Lists the possible "winning" combinations - for 3 in a row"""
        
        winning_pattern = [[0,1,2],[3,4,5],[6,7,8], # vertical
                        [0,3,6],[1,4,7],[2,5,8], # horizontal
                        [0,4,8],[2,4,6]]         # diagonal
        for row in winning_pattern:
            if self.pieces[row[0]] != Empty and allEqual([self.pieces[i] for i in row]):
                return self.pieces[row[0]]
            
    def getValidMoves(self):
        """Returns the list of possible remaining moves"""
        
        return [pos for pos in range(9) if self.pieces[pos] == Empty]
    
    def gameOver(self):
        """Returns true when the game is over - if one player has won/lost or if there
            are no more available moves (tie)."""
        
        return self.winner() or not self.getValidMoves()
    
    def makeMove(self, move, player):
        """Plays a move - but doesn't check if that move is actually available.
            Checking to make sure that move is open before playing it is done later."""
        
        self.pieces[move] = player
    
    def undoMove(self, move):
        """Takes away a move that was made - reopens that space on the board."""
        
        self.makeMove(move, Empty)

    def makeBoundaries(self, window):
        """Draws the Tic Tac Toe board in a GUI - draws an empty board"""
        
        rect1=Rectangle(Point(261,25),Point(282,775))
        rect1.setFill("blue")
        rect1.draw(window)
        rect2=Rectangle(Point(518,25),Point(539,775))
        rect2.setFill("blue")
        rect2.draw(window)
        rect3=Rectangle(Point(25,261),Point(775,282))
        rect3.setFill("blue")
        rect3.draw(window)
        rect4=Rectangle(Point(25,518),Point(775,539))
        rect4.setFill("blue")
        rect4.draw(window)

    def makeButtons(self, window):
        """Draws the the "Play Again" and "Quit" buttons"""
        
        playAgain=Rectangle(Point(820,725),Point(990,775))
        playAgain.setFill("blue")
        playAgain.draw(window)
        playAgain1=Text(Point(905,750),"Play Again")
        playAgain1.setSize(24)
        playAgain1.setTextColor("light blue")
        playAgain1.draw(window)
        quitChoice=Rectangle(Point(1010,725),Point(1180,775))
        quitChoice.setFill("blue")
        quitChoice.draw(window)
        quit1=Text(Point(1095,750),"Quit")
        quit1.setSize(24)
        quit1.setTextColor("light blue")
        quit1.draw(window)

    def showScoreboard(self, window, gamesPlayed, playerWins, computerWins, catScratches):
        """Draws the overall scoreboard for the game"""

        box=Rectangle(Point(820,20),Point(1140,260))
        box.setFill("blue")
        box.draw(window)
        games=Text(Point(955,50),"Games Played:")
        games.setSize(36)
        games.setTextColor("light blue")
        games.setStyle("italic")
        games.draw(window)
        games2=Text(Point(1110,50),gamesPlayed)
        games2.setSize(36)
        games2.setTextColor("light blue")
        games2.draw(window)
        player=Text(Point(935,110),"Player Wins:")
        player.setSize(36)
        player.setTextColor("light blue")
        player.setStyle("italic")
        player.draw(window)
        player2=Text(Point(1110,110),playerWins)
        player2.setSize(36)
        player2.setTextColor("light blue")
        player2.draw(window)
        comp=Text(Point(960,170),"Computer Wins:")
        comp.setSize(36)
        comp.setTextColor("light blue")
        comp.setStyle("italic")
        comp.draw(window)
        comp2=Text(Point(1110,170),computerWins)
        comp2.setSize(36)
        comp2.setTextColor("light blue")
        comp2.draw(window)
        scratch=Text(Point(950,230),"Cat Scratches:")
        scratch.setSize(36)
        scratch.setTextColor("light blue")
        scratch.setStyle("italic")
        scratch.draw(window)
        scratch2=Text(Point(1110,230),catScratches)
        scratch2.setSize(36)
        scratch2.setTextColor("light blue")
        scratch2.draw(window)

    def findBox(self, pt):
        """Figures out which box the user clicked in to determine where to play the
           user's move"""
        
        boxSpot = 0
        if pt.getX()>25 and pt.getX()<261:
            if pt.getY()>25 and pt.getY()<261:
                boxSpot=1
            if pt.getY()>282 and pt.getY()<518:
                boxSpot=4
            if pt.getY()>539 and pt.getY()<775:
                boxSpot=7
        elif pt.getX()>282 and pt.getX()<518:
            if pt.getY()>25 and pt.getY()<261:
                boxSpot=2
            if pt.getY()>282 and pt.getY()<518:
                boxSpot=5
            if pt.getY()>539 and pt.getY()<775:
                boxSpot=8
        elif pt.getX()>539 and pt.getX()<775:
            if pt.getY()>25 and pt.getY()<261:
                boxSpot=3
            if pt.getY()>282 and pt.getY()<518:
                boxSpot=6
            if pt.getY()>539 and pt.getY()<775:
                boxSpot=9
        return boxSpot
        
    def drawXorO(self, boxSpot, player, window):
        """Draws an "X" or "O" based on which player is currently playing"""
        
        if player=='o':
            if boxSpot==1:
                O=Circle(Point(143,143),100)
                Omiddle=Circle(Point(143,143),75)
            elif boxSpot==2:
                O=Circle(Point(400,143),100)
                Omiddle=Circle(Point(400,143),75)
            elif boxSpot==3:
                O=Circle(Point(657,143),100)
                Omiddle=Circle(Point(657,143),75)
            elif boxSpot==4:
                O=Circle(Point(143,400),100)
                Omiddle=Circle(Point(143,400),75)
            elif boxSpot==5:
                O=Circle(Point(400,400),100)
                Omiddle=Circle(Point(400,400),75)
            elif boxSpot==6:
                O=Circle(Point(657,400),100)
                Omiddle=Circle(Point(657,400),75)
            elif boxSpot==7:
                O=Circle(Point(143,657),100)
                Omiddle=Circle(Point(143,657),75)
            elif boxSpot==8:
                O=Circle(Point(400,657),100)
                Omiddle=Circle(Point(400,657),75)
            elif boxSpot==9:
                O=Circle(Point(657,657),100)
                Omiddle=Circle(Point(657,657),75)
            O.setOutline('black')
            O.setFill('red')
            O.draw(window)
            Omiddle.setOutline('black')
            Omiddle.setFill('light blue')
            Omiddle.draw(window)
        elif player=="x":
            if boxSpot==1:
                X=Line(Point(60,60),Point(226,226))
                X2=Line(Point(60,226),Point(226,60))
            elif boxSpot==2:
                X=Line(Point(317,60),Point(483,226))
                X2=Line(Point(317,226),Point(483,60))
            elif boxSpot==3:
                X=Line(Point(574,60),Point(740,226))
                X2=Line(Point(574,226),Point(740,60))
            elif boxSpot==4:
                X=Line(Point(60,317),Point(226,483))
                X2=Line(Point(60,483),Point(226,317))
            elif boxSpot==5:
                X=Line(Point(317,317),Point(483,483))
                X2=Line(Point(317,483),Point(483,317))
            elif boxSpot==6:
                X=Line(Point(574,317),Point(740,483))
                X2=Line(Point(574,483),Point(740,317))
            elif boxSpot==7:
                X=Line(Point(60,574),Point(226,740))
                X2=Line(Point(60,740),Point(226,574))
            elif boxSpot==8:
                X=Line(Point(317,574),Point(483,740))
                X2=Line(Point(317,740),Point(483,574))
            elif boxSpot==9:
                X=Line(Point(574,574),Point(740,740))
                X2=Line(Point(574,740),Point(740,574))
            X.setWidth(30)
            X.setFill('black')
            X.draw(window)
            X2.setWidth(30)
            X2.setFill('black')
            X2.draw(window)

    def displayPayoffs(self, moves, window):
        """Displays the given payoffs of each square for the computer (1 = win, 0 = tie, -1 = loss)"""
        
        label = Text(Point(0,0),'')
        label2 = Text(Point(0,0),'')
        label3 = Text(Point(0,0),'')
        label4 = Text(Point(0,0),'')
        label5 = Text(Point(0,0),'')
        label6 = Text(Point(0,0),'')
        label7 = Text(Point(0,0),'')
        label8 = Text(Point(0,0),'')
        label9 = Text(Point(0,0),'')
        
        for i in range(len(moves)):
            if moves[i][0]==0:
                label = Text(Point(143,143), '%s' % moves[i][1])
                label.setSize(36)
                label.setTextColor("red")
                label.draw(window)
            elif moves[i][0]==1:
                label2 = Text(Point(400,143), '%s' % moves[i][1])
                label2.setSize(36)
                label2.setTextColor("red")
                label2.draw(window)
            elif moves[i][0]==2:
                label3 = Text(Point(657,143), '%s' % moves[i][1])
                label3.setSize(36)
                label3.setTextColor("red")
                label3.draw(window)
            elif moves[i][0]==3:
                label4 = Text(Point(143,400), '%s' % moves[i][1])
                label4.setSize(36)
                label4.setTextColor("red")
                label4.draw(window)
            elif moves[i][0]==4:
                label5 = Text(Point(400,400), '%s' % moves[i][1])
                label5.setSize(36)
                label5.setTextColor("red")
                label5.draw(window)
            elif moves[i][0]==5:
                label6 = Text(Point(657,400), '%s' % moves[i][1])
                label6.setSize(36)
                label6.setTextColor("red")
                label6.draw(window)
            elif moves[i][0]==6:
                label7 = Text(Point(143,657), '%s' % moves[i][1])
                label7.setSize(36)
                label7.setTextColor("red")
                label7.draw(window)
            elif moves[i][0]==7:
                label8 = Text(Point(400,657), '%s' % moves[i][1])
                label8.setSize(36)
                label8.setTextColor("red")
                label8.draw(window)
            elif moves[i][0]==8:
                label9 = Text(Point(657,657), '%s' % moves[i][1])
                label9.setSize(36)
                label9.setTextColor("red")
                label9.draw(window)
            time.sleep(0)
            
        label.undraw()
        label2.undraw()
        label3.undraw()
        label4.undraw()
        label5.undraw()
        label6.undraw()
        label7.undraw()
        label8.undraw()
        label9.undraw()
                
def humanPlayer(board, player, window):
    """Plays for the user - allows user to make moves in the GUI and documents
        what moves their making (so computer can then react)"""
    
    point = window.getMouse()
    move = board.findBox(point)
    while move == 0 or move in usedBoxes:
        point = window.getMouse()
        move = board.findBox(point)
    board.drawXorO(move, player, window)
    board.makeMove(move-1, player)
    usedBoxes.append(move)
    
def computerPlayer(board, player, window):
    """Plays for the computer - allows computer to make moves in the GUI"""

    opponent = { Computer : User, User : Computer }

    def judge(winner):
        """Awards a score based on who wins the game: a +1 for a win, 0 for a tie and
            -1 for a loss"""
        
        if winner == player:
            return +1
        if winner == None:
            return 0
        return -1
    
    def evaluateMove(move, p=player):
        """Evaluates every node as it traverses through the game tree"""
        
        try:
            board.makeMove(move, p)
            if board.gameOver():
                return judge(board.winner())
            outcomes = (evaluateMove(next_move, opponent[p]) for next_move in board.getValidMoves())
            if p == player:
                min_element = 1
                for o in outcomes:
                    if o == -1:
                        return o
                    min_element = min(o,min_element)
                return min_element
            else:
                max_element = -1
                for o in outcomes:
                    if o == +1:
                        return o
                    max_element = max(o,max_element)
                return max_element
        finally:
            board.undoMove(move)

    # creates a list of possible VALID moves and then sorts them in terms of which yields
    # the highest profit
    moves = [(move, evaluateMove(move)) for move in board.getValidMoves()]
    random.shuffle(moves)
    moves.sort(key = lambda (move, winner): winner)
    board.makeMove(moves[-1][0], player)
    board.displayPayoffs(moves, window)
    choice = moves[-1][0]
    board.drawXorO(choice+1, player, window)
    usedBoxes.append(choice+1)
    
def game(gamesPlayed, playerWins, computerWins, catScratches, usedBoxes):
    """This function creates/plays the actual game. Builds the game board in the GUI
        and calls the functions above (computerPlayer and humanPlayer) to play out
        the game."""
    
    b = Board()
    window=GraphWin("Tic Tac Toe!",1200,800)
    window.setBackground("light blue")
    b.makeBoundaries(window)
    b.makeButtons(window)
    b.showScoreboard(window, gamesPlayed, playerWins, computerWins, catScratches)

    firstMove = random.randrange(2)
    
    if firstMove == 0:
        User = 'x'
        Computer = 'o'
    elif firstMove == 1:
        User = 'x'
        Computer = 'o'
        
    while True:
        if User == 'x':
            humanPlayer(b, User, window)
            if b.gameOver(): 
                break
            computerPlayer(b, Computer, window)
            if b.gameOver(): 
                break
        elif Computer == 'x':
            computerPlayer(b, Computer, window)
            if b.gameOver(): 
                break
            humanPlayer(b, User, window)
            if b.gameOver(): 
                break

    # if there is a winner, outputs who that winner is
    if b.winner():
        if User == b.winner():
            playerWins += 1
            label = Text(Point(930,110), 'Player Wins')
            label.setSize(36)
            label.setTextColor("red")
            label.setStyle("italic")
            label.draw(window)
        elif Computer == b.winner():
            computerWins += 1
            label = Text(Point(955,170), 'Computer Wins')
            label.setSize(36)
            label.setTextColor("red")
            label.setStyle("italic")
            label.draw(window)
    # if the game is a tie, outputs that the result is a tie
    else:
        label = Text(Point(945,230), "Cat Scratches")
        label.setSize(36)
        label.setTextColor("red")
        label.setStyle("italic")
        label.draw(window)
        catScratches += 1
        
    while True:
        pt=window.getMouse()
        if 820<pt.getX()<990 and 725<pt.getY()<775:
            del usedBoxes[:]
            if firstMove == 0:
                firstMove = 1
            elif firstMove == 1:
                firstMove = 0
            ## runs the game function - serves to use all the rules of the game
            ## and has the computer using the mini max
            window.close()
            gamesPlayed += 1
            game(gamesPlayed, playerWins, computerWins, catScratches, usedBoxes)
            break
        elif 1010<pt.getX()<1180 and 725<pt.getY()<775:
            window.close()
            break                

if __name__ == "__main__":
    gamesPlayed = 0
    playerWins = 0
    computerWins = 0
    catScratches = 0
    # list of spaces that are "used" = have been played in - starts at 0 (board is empty)
    usedBoxes = []
    game(gamesPlayed, playerWins, computerWins, catScratches, usedBoxes)
