# Author: Lemfon Karl Ndze'dzenyuy
# Date: 20/01/2019
# Goal: This program is supposed to calculate the slope of a non-vertical line

#Writing a function to calculate the slope
def slopeCalculator(x1,y1,x2,y2):
    return ((y2 - y1)/(x2 - x1))

# Obtaining the values from the user
px1,py1 = eval(input("Enter the coordinates of the first point, seperate them with a comma please: "))
px2, py2 = eval(input("Enter the coordinates of the second point, seperate them with a comma please: "))
# Ensuring that the line is non-vertical
if px2 == px1:
    print("Sorry your line is vertical")
else:
    if slopeCalculator(px1,py1,px2,py2) != 0:
        print("The slope of your line is ", slopeCalculator(px1, py1, px2, py2))
    else:
        print("The slope of your line is ", slopeCalculator(px1, py1, px2, py2), ".Meaning it is a horizontal line")
