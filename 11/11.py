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

res=0
emptycol=[True]*len(lines[0])
emptyline="."*len(lines[0])
newlines=[]
for line in lines:
    if line==emptyline:
        newlines.append(emptyline)
    newlines.append(line)
    for i, c in enumerate(line):
        if c == '#':
            emptycol[i]=False

lines = []
stars = []
for y, newline in enumerate(newlines):
    line = ""
    for i, c in enumerate(newline):
        if emptycol[i]:
            line+='.'
        line+=c
    lines.append(line)
    for x,c in enumerate(line):
        if line[x]=='#':
            stars.append((y,x))

for i, star in enumerate(stars):
    for j in range(i+1,len(stars)):
        res+=abs(star[0]-stars[j][0])
        res+=abs(star[1]-stars[j][1])


print(res)
