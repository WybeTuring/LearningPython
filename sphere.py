# Author: Lemfon Karl Ndze'dzenyuy
# Date: 20/01/2019
# Goal: This program is supposed to calculate the volume and surface area of a sphere

import math
# Function to calculate the surface area
def surfaceArea(r):
    return (4*math.pi*(r**2))
def volume(r):
    return ((4/3)*math.pi*(r**3))

# Getting the values from the user
radius = eval(input("Enter the radius of your sphere: "))
print("The volume of a sphere with radius", radius, "is", volume(radius))
print("The surface area of a sphere with radius", radius, "is", surfaceArea(radius))
