def summing():
    num = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ans = input('Enter the name: ').lower()
    sum = 0
    for c in ans:
        sum += num.index(c)
    print(sum)

def summing2():
    ans = input('Enter the name: ').lower()
    sum = 0
    for i in ans:
        print(ord(i) - 96) # Take note of the fact that small letters start from 97!
        sum += (ord(i) - 96)
    print(sum)

summing()
