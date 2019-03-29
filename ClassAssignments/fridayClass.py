from graphics import *
def main():
    win = GraphWin("FaceDraw", 500, 500)
    # Draw the head head using circle object
    head= Circle(Point(win.getWidth()/2, win.getHeight()/2), 100)
    head.draw(win)
    # Draw the left eye using a circle object
    lefteye = Circle(Point(210,210),15)
    lefteye.draw(win)
    # Draw the right eye by cloning the lefy eye and moving it 80 pixels to the right
    righteye = lefteye.clone()
    righteye.move(80,0)
    righteye.draw(win)
    # Draw the mouth as a horizontal line
    mouth = Line(Point(230,300),Point(270,300))
    mouth.draw(win)
    # Draw the nose as a triangle
    message = Text(Point(win.getWidth()/2, 20), 'Click on three points to draw the nose')
    message.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    nose = Polygon(point1,point2,point3)
    # nose = Polygon(Point(250,240),Point(240, 260),Point(260, 260))
    nose.draw(win)
    message.setText('Click anywhere to close')
    
    win.getMouse()
    win.close()

main()
    


