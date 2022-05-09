# given 2 dimensions as input (n and 3n) print a design similar to this (generated with 9 and 27 as input)
#------------.|.------------
#---------.|..|..|.---------
#------.|..|..|..|..|.------
#---.|..|..|..|..|..|..|.---
#----------WELCOME----------
#---.|..|..|..|..|..|..|.---
#------.|..|..|..|..|.------
#---------.|..|..|.---------
#------------.|.------------

ins = input()
h, w = ins.split(" ")
height = int(h)
width = int(w)
mid = ".|."
mirror = []
count = [x for x in range(1,height-1,2)]

for x in range(0,height+1):
    if x < (height)//2:
        line = (count[x]*mid).center(width,"-")
        print(line)
        mirror.append(line)
    elif x == (height+1)//2:
        line = "WELCOME".center(width,"-")
        print(line)
    elif x > (height)//2:
        print(mirror.pop())
