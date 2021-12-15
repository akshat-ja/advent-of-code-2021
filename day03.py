import sys

length = 0
count = 0

binaries = []
gbin = 0
ebin = 0
gamma = 0 # 1s and 0s
epsilon = 0 # 0s and 1s (inverted)

with open('day03.in', 'r') as openfile:
    openlines = openfile.readlines()
    
    length = len(openlines[0]) - 1
    count = len(openlines)
    
    binaries = [0] * length
    
    print(length)
    print(count)
    
    for line in openlines:
        inline = str(line.strip())
        print(inline)
        i = 0
        for num in str(inline):
            print(num, " ", i)
            if int(num) > 0:
                binaries[i] += 1
            i += 1
            
    print(binaries)
    
    base = 11
    for num in binaries:
        if num > count/2:
            gamma += 2**base
            gbin += 10**base
            print('g')
        else:
            epsilon += 2**base
            ebin += 10**base
            print('e')
        base -= 1
        print(num, ' ', count/2)
        
    print(gamma)
    print(epsilon)
    print(gbin)
    print(ebin)
    print(gamma*epsilon)