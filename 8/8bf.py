#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re

#f = open("8/sample2.raw", "r")
f = open("8/in.raw", "r")
lines = f.read().splitlines()

turns = lines[0]
res = 0
map=dict()
for i in range(2,len(lines)):
    src,dst = lines[i].split(' = ')
    dstl,dstr = dst[1:-1].split(', ')
    map[src]=(dstl,dstr)
pprint(turns)
pprint(map)
pos='AAA'
while False: #pos!='ZZZ':
    turn = 0 if turns[res%len(turns)]=='L' else 1
    pos = map[pos][turn]
    res+=1
    #print(turn,pos)
print(res)

res=0
pos = [p for p in map.keys() if p[-1]=='A']
while len(set([l[-1] for l in pos]))!=1 or pos[0][-1]!='Z':
    for i in range(len(pos)):
            turn = 0 if turns[res%len(turns)]=='L' else 1
            pos[i]=map[pos[i]][turn]
    res+=1
print(res)