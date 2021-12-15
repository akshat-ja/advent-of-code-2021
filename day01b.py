import sys

inline = 0
lastline = -1
depth = 0

increases = 0
decreases = 0

length = 0

with open('day01.in', 'r') as openfile:
    openlines = openfile.readlines()
    length = len(openlines)
    
    for i in range(0, length-2):
        print(openlines[i], openlines[i+1], openlines[i+2])
        inline = int(openlines[i]) + int(openlines[i+1]) + int(openlines[i+2])
    
        if lastline > 0:
            if inline > lastline:
#               print(inline, ' (increased)', depth)
                depth +=1
                increases += 1
            else:
#                print(inline, ' (decreased)', depth)
                depth -=1
                decreases += 1
        else:
#            print(inline, ' (no change)')
            pass
        lastline = inline
        
print(increases)