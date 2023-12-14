#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
import copy

f = open("14/in.raw", "r")
#f = open("14/sample.raw", "r")
rawlines = f.read().splitlines()

# Part 1
lines = [list(s) for s in rawlines]

topmost = [-1]*len(lines[0])
weight=0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "O":
            topmost[j]+=1
            weight+=len(lines)-topmost[j]
        elif c== "#":
            topmost[j]=i
print('Part 1:', weight)

#part 2
lines = [list(s) for s in rawlines]

def fall(direction,lines):
    if (direction==0 or direction==1):
        topmost = [-1]*len(lines[0])
        increment = 1
    else:
        topmost = [len(lines)]*len(lines[0])
        increment = -1
    for i in range(len(lines)):
        for j in range(len(lines)):
            if direction==0: #N
                row = i
                column = j
            elif direction==1: #W
                row = j
                column = i
            elif direction==2: #S
                row = len(lines)-1-i
                column = j
            else: #direction==3 #E
                row = j
                column = len(lines)-1-i
            if lines[row][column] == "O":
                topmost[j] += increment
                lines[row][column] = '.'
                if direction in [0,2]:
                    lines[topmost[j]][column] = 'O'
                else:
                    lines[row][topmost[j]] = 'O'
            elif lines[row][column] == "#":
                if direction in [0,2]:
                    topmost[j] = row
                else:
                    topmost[j] = column
    #print()
    #print(f'moved in {direction}')
    #for line in lines:
    #    print(''.join(line))
    #print()

#print(weight(lines))
#print()
#print(f'starting pos')
#for line in lines:
#    print(''.join(line))
#print()

def findloop(lines):
    seen={}
    seen[''.join([''.join(line) for line in lines])] = (-1,-1)
    for i in range(1000000000):
        for dir in range(4):
            fall(dir,lines)
        newseen=''.join([''.join(line) for line in lines])
        if newseen in seen:
            return(i, i - seen[newseen])
        else:
            seen[newseen]=i

first, loopsize = findloop(lines)
print(i)
for i in range((1000000000-first)%loopsize-1):
    for dir in range(4):
        fall(dir,lines)
res=0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=='O':
            res+=len(lines)-i 
print(res)
