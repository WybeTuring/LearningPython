rain = open('rainfall.txt','r')
rainInches = open('karl.txt','w')
for aline in rain:
    values = aline.split()
    print(values[0] + ' ' +  str(float(values[1])*2.54) + ' centimeters of rain',file=rainInches)
rainInches.close()
rain.close()