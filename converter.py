# Author: Lemfon Karl Ndze'dzenyuy
# Date: 20/01/2019
# Goal: This program is supposed to converts temperatures from fahrenheit to Celcius

# Writing a function that does the conversion
def convertTemp(tf):
    return ((tf - 32)*(5/9))

# Getting the values from the userf and printing the result
temp = eval(input("Enter the temperature in fahrenheit: "))
print("The equivalent in Celcius is", convertTemp(temp))
