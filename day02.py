import sys

xdir = 0 # forward
ydir = 0 # up, down

inline = []

with open('day02.in', 'r') as openfile:
    openlines = openfile.readlines()
    
    for line in openlines:
        inline = line.strip().split(" ")
        #print(inline)
        if 'forward' in inline[0]:
            print('f', inline[1])
            xdir += int(inline[1])
        elif 'up' in inline[0]:
            print('u', inline[1])
            ydir -= int(inline[1])          
        elif 'down' in inline[0]:
            print('d', inline[1])
            ydir += int(inline[1])
            
print('x', xdir)
print('y', ydir)
print(xdir*ydir)