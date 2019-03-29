from graphics import *
nw = GraphWin("Graphics", 600, 600)
k = Point(nw.getWidth()/2, nw.getHeight()/2)
k.draw(nw)
circ = Circle(k,40)
circ.draw(nw)
i = nw.getMouse()
cr = Circle(i, 30)
cen = cr.getCenter()
cr.draw(nw)
print(cen.getX(), cen.getY())
print(i.getX(), i.getY())
j = nw.getKey()
print(j)
rec = Rectangle(Point(20,40), Point(60,10))
rec.draw(nw)


nw.close
