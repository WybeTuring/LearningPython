def maximum(ls):
    ans = ls[0]
    for k in range(1,len(ls)):
        if ls[k] > ans:
            ans = ls[k]
    return ans

li = [4, 8, 5, 10, 2]
print(maximum(li))
ls = input("Enter your values, seperate them with spaces: ").split()
for k in range(len(ls)):
    ls[k] = float(ls[k])
print(type(maximum(ls)))
