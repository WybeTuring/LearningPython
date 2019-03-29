from graphics import *
def face():
    win = GraphWin("Ziba", 600, 600)
    circ = Circle(Point(win.getWidth()/2, win.getHeight()/2), 200)
    circ.draw(win)
    circ.setFill("blue")

face()
    
