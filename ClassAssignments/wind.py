def windChill(t,v):
    return (35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16))
def main():
    print("{0:10}".format(" "), end = '\t')
    for k in range(-20,61,10):
        print('{0:>10}'.format("T = " + str(k)), end = '\t')
    print()
    for p in range(0,51,5):
        print('{0:<10}'.format("V = " + str(p)), end = '\t')
        for k in range(-20,61,10):
            print('{0:>10.2f}'.format(windChill(k,p)), end = '\t')
        print()
main()
    
            
