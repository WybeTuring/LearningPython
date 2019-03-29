def unique():
    ls=[4, 15, 5, 21, 100, 3, 22, 45, 87, 56]
    a=eval(input("Try guessing a number which is not on my hidden list: "))
    if a in ls:
        print("The number is not unique ")
        unique()
    else:
        print("Congratulations!!")
unique()
