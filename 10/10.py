#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("10/in.raw", "r")
#f = open("10/sample.raw", "r")
lines = f.read().splitlines()


def printmap(lines):
    for pipemapl in lines:
        print("".join(pipemapl))

i=0
s_pos = -1
while s_pos==-1:
    s_pos = lines[i].find('S')
    i+=1
s_pos=(i-1,s_pos)
pos=s_pos
if lines[s_pos[0]-1][s_pos[1]] in "7F|":
    pos=(s_pos[0]-1,s_pos[1])
    move=0
elif lines[s_pos[0]][s_pos[1]+1] in "-J7":
    pos=(s_pos[0],s_pos[1]+1)
    move=1
elif lines[s_pos[0]+1][s_pos[1]] in "|LJ":
    pos=(s_pos[0]+1,s_pos[1])
    move=2
res = 1
# The 4-tuple is (Y-inc,X-inc,NewDirection,Clockwise,Clockwise(Inner,Outer),CounterClockwise(Inner,Outer))
D=[
    {'|':(-1,0,0,0,
          ([(0,1)],[(0,-1)])),
     'F':(0,1,1,1,
          ([(1,1)],[(-1,-1),(0,-1),(-1,0)])),
     '7':(0,-1,3,-1,
          ([(-1,1),(0,1),(-1,0)],[(1,-1)]))},
    {'-':(0,1,1,0,
          ([(1,0)],[(-1,0)])),
     '7':(1,0,2,1,
          ([(1,-1)],[(-1,1),(0,1),(-1,0)])),
     'J':(-1,0,0,-1,
          ([(1,1),(0,1),(1,0)],[(-1,-1)]))},
    {'|':(1,0,2,0,
          ([(0,-1)],[(0,1)])),
     'J':(0,-1,3,1,
          ([(-1,-1)],[(1,1),(0,1),(1,0)])),
     'L':(0,1,1,-1,
          ([(1,-1),(0,-1),(1,0)],[(-1,1)]))},
    {'-':(0,-1,3,0,
          ([(-1,0)],[(1,0)])),
     'L':(-1,0,0,1,
          ([(-1,1)],[(1,-1),(0,-1),(1,0)])),
     'F':(1,0,2,-1,
          ([(-1,-1),(0,-1),(-1,0)],[(1,1)]))}
]
pipemap = [['#']*len(lines[0]) for _ in range(len(lines))]
pipemap[s_pos[0]][s_pos[1]]='S'
clock=0
first_pos=pos
first_move=move
while pos!=s_pos:
    pipemap[pos[0]][pos[1]]=lines[pos[0]][pos[1]]
    DATA=D[move][lines[pos[0]][pos[1]]]
    clock+=DATA[3]
    new_pos=(pos[0]+DATA[0],
             pos[1]+DATA[1])
    move=DATA[2]
    pos = new_pos
    res+=1
print(res)
print(res/2)
print(clock)
lines=[["#"]+pml+["#"] for pml in pipemap]
lines=[["#"]*len(lines[0])]+lines+[["#"]*len(lines[0])]
pos=(first_pos[0]+1, first_pos[1]+1)
s_pos=(s_pos[0]+1, s_pos[1]+1)
move=first_move
if clock==4:
    clockwise=True
elif clock==-4:
    clockwise=False
else:
    print('FAIL')
    exit()
res=0
while pos!=s_pos:
    DATA=D[move][lines[pos[0]][pos[1]]]
    if clockwise:
        IN=DATA[4][0]
        OUT=DATA[4][1]
    else:
        IN=DATA[4][1]
        OUT=DATA[4][0]
    for is_in in IN:
        v=lines[pos[0]+is_in[0]][pos[1]+is_in[1]]
        if v=="#":
            lines[pos[0]+is_in[0]][pos[1]+is_in[1]]='I'
        elif v=="O":
            print('FAIL')
            exit()
    for is_out in OUT:
        v=lines[pos[0]+is_out[0]][pos[1]+is_out[1]]
        if v=="#":
            lines[pos[0]+is_out[0]][pos[1]+is_out[1]]='O'
        elif v=="I":
            printmap(lines)
            print('FAIL')
            pprint(pos)
            exit()
    new_pos=(pos[0]+DATA[0],
             pos[1]+DATA[1])
    move=DATA[2]
    pos = new_pos
    res+=1
#count I's
res=0
for line in lines:
    strline="".join(line)
    # Fill "inner big spaces"
    while strline.find('I#')!=-1:
        ini=strline.find('I#')
        end=strline.find('#I')
        strline=strline[:ini]+'I'*(end-ini+2)+strline[end+2:]
    res+=strline.count('I')
    print(strline,strline.count('I'),res)
print(res)
