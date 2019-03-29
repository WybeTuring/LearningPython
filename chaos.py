# Author: Lemfon Karl Ndze'dzenyuy
# Date: 20/01/2019
# Goal: This program modifies the chaos program to allow the user to choose the number of values to printing

def main(num):
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(num):
        x = 3.9 * x * (1 - x)
        print(x)
numberOfTimes = int(input("Enter the number of times you want to print values of the chaotic function: "))
main(numberOfTimes)
