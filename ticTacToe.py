# Nitin George
# ticTacToe.py
#
# Problem: Develop a program that uses indefinite loops to play TicTacToe.
#
#Certificate of Authenticity:
#I certify that this lab is entirely my own work.
from graphics import *
import time

#Input:
#Output:list of nums for board
def buildBoard():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list

def displayBoard(lst):
    for i in range(0,9,3):
        print(lst[i:i+3])

#Input: list, i.e. board with spots, and Spot
#that user wants to place char in
#Output: True if spot is Legal, False if not
def isLegal(board, spot):
    return board[spot-1] != "X" and board[spot-1] != "O"

#Input: Board, Spot, Char same as last but with Char this time
#Output: void but board should now have spots filled
def fillSpot(board, spot, char):
    board[spot-1] = char
    
#Input: board
#Output: True if game is won, False if not
def isGameWon(board):
    winningPlay = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
                   (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

#For each iteration in the list, the function searches each char at the
#respective position and if they match, it returns True, else False.
    
    for play in winningPlay:
        if board[play[0]] == board[play[1]] == board[play[2]]:
            return True
    return False
    

def charLoop( numPlays):
    if numPlays%2 == 1:
        char = "X"
        return char
        
    else:
        char = "O"
        return char

##Input: board again, and number of Plays left/done.
##Output: True isGameWon == True or True if number of Plays are done.
def isGameOver(board, numPlays):
    if isGameWon(board) == True or numPlays == 0:
        return True


def playGame():
##    while button == True:
    win = GraphWin("ticTacToe", 300, 300)
    win.setCoords(0, 3, 3, 0)
    win.setBackground('white')

    vLine1= Line(Point(1,0), Point(1,3))
    vLine1.draw(win)
    vLine2= Line(Point(2,0), Point(2,3))
    vLine2.draw(win)

    hLine1= Line(Point(0,1), Point(3,1))
    hLine1.draw(win)
    hLine2= Line(Point(0,2), Point(3,2))
    hLine2.draw(win)
    
    numPlays = 9
    board = buildBoard()

    while isGameOver(board, numPlays) != True:
        p = win.getMouse()
        x = int(p.getX() // 1)
        y = int(p.getY() // 1)        
        spot = y * 3 + x + 1

        char = charLoop(numPlays)
        if char == "X":
            xLine1 = Line(Point(x+0.25, y+0.25), Point(x+0.75, y+0.75))
            xLine1.draw(win)
            yLine2 = Line(Point(x+0.75, y+0.25), Point(x+0.25, y+0.75))
            yLine2.draw(win)

        else:
            o = Circle(Point(x+0.5,y+0.5), 0.45)
            o.draw(win)


        if isLegal(board, spot) == True:
            fillSpot(board, spot, char)
            numPlays -=1

        if isGameWon(board) == True:
            msg = Text(Point(1.5,1.5),f"YOU WIN YAHOOOO!!!! {char} wins")
            msg.draw(win)
            msg.setFill("blue")
            break
        elif isGameOver(board, numPlays) == True:
            msg = Text(Point(1.5,1.5),"GAME DONE!!!!, TIE :((")
            msg.draw(win)
            msg.setFill("blue")

    button = Rectangle(Point(.5,2.4), Point(1.4, 2.8))
    button.setOutline("red")
    button.setFill("red2")
    button.draw(win)
    butTxt = Text(Point(1,2.6), "Try again")
    butTxt.draw(win)
    
    button2 = Rectangle(Point(1.6,2.4), Point(2.5, 2.8))
    button2.setOutline("green")
    button2.setFill("green4")
    button2.draw(win)
    butTxt2 = Text(Point(2.1,2.6), "Close")
    butTxt2.draw(win)

    click = win.getMouse()
    cX = click.getX()
    cY = click.getY()

    if cX < 1.4 and cX > .5 and cY < 2.8 and cY > 2.4:
        button.setFill("red4")
        win.close()
        playGame()
    elif cX < 2.5 and cX > 1.6 and cY < 2.8 and cY > 2.4:
        button2.setFill("green2")
        msg.setText("BYEBYE")
        time.sleep(1)
        win.close()

playGame()
    
