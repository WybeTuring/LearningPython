from math import sqrt
def syr(x):
    seq = [x]
    while x != 1:
        if x%2 == 0:
            x = x/2
            seq.append(int(x))
        else:
            x = (3*x) + 1
            seq.append(x)
    return seq

def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0 : return False
    return True

def primedet(n):
    ans = []
    for i in range(2,n+1):
        if prime(i): ans.append(i)
    return ans


def golbach(n):
    if n%2 !=0: return ("Please the number you entered is not prime")
    else:
        for r in range(2,n+1):
           if n -r > 0:
               for i in range(2,n-r+1):
                   if (r + i == n) and (prime(r) and prime(i)):
                       return (r,i)
def golbach2(n):
    ans = []
    for i in range(n):
        if prime(i):ans.append(i)
    ans2 = ans[::-1]
    for i in range(len(ans2)):
        for j in range(len(ans)):
            if ans[i] + ans2[j] == n:
                return ans[i],ans2[j]

print(golbach2(222))

           
                
        
    
