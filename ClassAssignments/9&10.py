from math import pi
class Spheres:
    def __init__(self, radius):
        self.radius = radius
        self.area = 4*pi*(radius**2)
        self.volume = (4/3)*pi*(radius**3)

philip = Spheres(4)
print(philip.radius)
print(philip.area)
print(philip.volume)

class Cube:
    def __init__(self, side):
        self.side = side
        self.area = 6 * (side**2)
        self.volume  = side**3

karl = Cube(5)
print(karl.side)
print(karl.area)
print(karl.volume)
