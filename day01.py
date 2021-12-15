import sys

inline = 0
lastline = -1
depth = 0

increases = 0
decreases = 0

with open('day01.in', 'r') as openfile:
    openlines = openfile.readlines()
    print(len(openlines))
    for line in openlines:
        inline = int(line.strip())
        if lastline > 0:
            if inline > lastline:
                print(inline, ' (increased)', depth)
                depth +=1
                increases += 1
            else:
                print(inline, ' (decreased)', depth)
                depth -=1
                decreases += 1
        else:
            print(inline, ' (no change)')
        lastline = inline
        
print(increases)