def gcd(m,n):
    while n:
        m, n = n, m%n
    return m
def main():
    j = eval(input("Please enter the largest number of the two: "))
    k = eval(input("Please enter the smaller number: "))
    try:
        print("The GCD of", j, "and", k, "is: ", gcd(j,k))
    except:
        print("Please ensure that you are following the instructions. Try again")
main()
    
    
