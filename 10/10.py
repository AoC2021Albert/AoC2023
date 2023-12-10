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
D=[
    {'|':(-1,0,0),
     'F':(0,1,1),
     '7':(0,-1,3)},
    {'-':(0,1,1),
     '7':(1,0,2),
     'J':(-1,0,0)},
    {'|':(1,0,2),
     'J':(0,-1,3),
     'L':(0,1,1)},
    {'-':(0,-1,3),
     'L':(-1,0,0),
     'F':(1,0,2)}
]
while pos!=s_pos:
    new_pos=(pos[0]+D[move][lines[pos[0]][pos[1]]][0],
             pos[1]+D[move][lines[pos[0]][pos[1]]][1])
    move=D[move][lines[pos[0]][pos[1]]][2]
    pos = new_pos
    res+=1
print(res)
print(res/2)

