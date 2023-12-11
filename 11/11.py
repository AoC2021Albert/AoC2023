#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("11/in.raw", "r")
#f = open("11/sample.raw", "r")
lines = f.read().splitlines()

EXPANSE=999999
res=0
offsetcols=[0]*len(lines[0])
offsetlines=[0]*len(lines)
emptycols=[True]*len(lines[0])
emptyline="."*len(lines[0])
for i, line in enumerate(lines):
    if line==emptyline:
        for j in range(i+1,len(lines)):
           offsetlines[j]+=EXPANSE
    for i, c in enumerate(line):
        if c == '#':
            emptycols[i]=False
for i, empty in enumerate(emptycols):
    if empty:
        for j in range(i+1,len(lines[0])):
            offsetcols[j]+=EXPANSE
stars = []
print(offsetlines,offsetcols)

for y, line in enumerate(lines):
    for x,c in enumerate(line):
        if line[x]=='#':
            print(f'start at {(y,x)} goes to {(y+offsetlines[y],x+offsetcols[x])}')
            stars.append((y+offsetlines[y],x+offsetcols[x]))

for i, star in enumerate(stars):
    for j in range(i+1,len(stars)):
        pprint((star,stars[j]))
        res+=abs(star[0]-stars[j][0])
        print(res)
        res+=abs(star[1]-stars[j][1])
        print(res)


print(res)
