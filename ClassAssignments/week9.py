i = 0
def main():
    from random import randrange
    heads, tails = 0, 0
    for i in range(50):
        h = randrange(1,3)
        if h == 1:
            heads += 1
        if h == 2:
            tails += 1
    print("The simulation generated", heads, "heads")
    print("The simulation generated", tails, "tails")
def main2():
    global i
    x = eval(input("How many times to do want 50 similuations: "))
    for i in range(x):
        print("\n")
        print("This is the", i, "iteration")
        i += 1
        main()
main2()
