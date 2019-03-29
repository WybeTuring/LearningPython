from random import random

def simOneGame(probA, probB):
    scoreA = scoreB = 0
    serving = "A"
    while not (scoreA == 15  or scoreB == 15):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() > probA:
                scoreB += 1
            else:
                serving = "A"
    return (scoreA, scoreB)

def simNGames(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        k = simOneGame(probA, probB)
        if k[0] > k[1]:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def main():
    probA = eval(input("Please enter the probability of A winning: "))
    probB = eval(input("Please enter the probability of B winning: "))
    n = int(input("Please enter the number of times you want to play: "))
    print(simNGames(n, probA, probB))
    
def vollyBall(probA, probB):
    scoreA = scoreB = 0
    serving = "A"
    while not((scoreA >=15 and ((scoreA - ScoreB) >= 2)) or (scoreB >= 15 and (scoreB - scoreA) >= 2)):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() > probA:
                scoreB += 1
            else:
                serving = "A"
    return (scoreA, scoreB)
        
                
                
        
