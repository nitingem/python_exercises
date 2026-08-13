# Nitin George
# valentineGreeting.py
#
# Problem: To make a cute valentines card.
#
#Certificate of Authenticity:
#I certify that this lab is entirely my own work.

from graphics import *
import math

def valentine():

    winWidth = 750
    winHeight = 500
    
    win = GraphWin("Happy Valentines" , winWidth, winHeight)
    win.setBackground("pink")
    
    heart1 = Circle(Point(2*winWidth/5, winHeight/3), 100)
    heart1.draw(win)
    heart1.setOutline("red")
    heart1.setFill("red")

    heart2 = heart1.clone()
    heart2.move(winWidth/5, 0)
    heart2.draw(win)
    
    heart3 = Polygon(Point(375,104), Point(224,232),
                     Point(375,404), Point(526,232))
    heart3.setOutline("red")
    heart3.setFill("red")
    heart3.draw(win)
#all three "hearts" are parts of the actual heart, with the two circles
#being the little bumps and the polygon being the sharp tip.
    
    arrow1 = Rectangle(Point(0, 245), Point(200, 255))
    arrow1.setOutline("brown")
    arrow1.setFill("brown")
    arrow1.draw(win)

    arrow2 = Polygon(Point(200, 260), Point(200, 240), Point(215, 250))
    arrow2.setOutline("brown")
    arrow2.setFill("brown")
    arrow2.draw(win)

    pt = Point(winWidth/2, winHeight-20)
    inst = Text(pt, "click to shoot an arrow")
    inst.draw(win)
    clickPt = win.getMouse()
    
    for i in range(8):
        arrow1.move(20, 0)
        arrow2.move(20, 0)
        time.sleep(.01)
#this makes the animation. I like animation so i tried to make it look smooth.

    inst.setText("Click for an additional surprise")
    clickPt = win.getMouse()

    win.setBackground("red")
    
    heart1.setFill("pink")
    heart1.setOutline("pink")
    heart2.setFill("pink")
    heart2.setOutline("pink")
    heart3.setFill("pink")
    heart3.setOutline("pink")
    arrow1.undraw()
    arrow2.undraw()

    inst.setText("!!!Happy Valentines Day!!!")
    inst.setSize(20)
    inst.setTextColor("white")

    for i in range(10):
        heart1.move(0,-5)
        heart2.move(0,-5)
        heart3.move(0,-5)
        time.sleep(.1)
        heart1.move(0,5)
        heart2.move(0,5)
        heart3.move(0,5)
        time.sleep(1)
    
valentine()
