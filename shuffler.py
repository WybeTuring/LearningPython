# I am writing a program that will shuffle the elements in a lsit, without using the shuffle method in random
def shuff(ls):
    import random;
    ks = []
    while len(ks) != len(ls):
        i = random.randint(0,len(ls)); # Randomly generates a positive interger that is less than the length
        if (not i in ks) and (i < len(ls)): # Ensures that the number is in the range and that it is not repeating
            ks.append(i);
    for k in range(0, len(ls)):
        ls[k] = ls[ks[k]]; # using the values of ks, which have been randomly chossen to change the values of ls
    return ls;

print(shuff([1,3,5,6,7,8,9,0,12,13]));
