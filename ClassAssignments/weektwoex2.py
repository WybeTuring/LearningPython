def converter(string, temp):
    string = string.upper()
    if string == 'CTOF':
        return ((5/9)*(temp - 32))
    elif string == 'FTOC':
        return ((9/5)*temp +32)
    else:
        print("Please enter a valid input")




