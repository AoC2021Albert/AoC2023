#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("23/in.raw", "r")
#f = open("23/sample.raw", "r")
lines = f.read().splitlines()
res = 0
y,x=0,1
fy=len(lines)-1

slopedir=('^','>','v','<')

def solve(y,x):
    dq = deque([(y,x,[(y,x)],)])
    while dq:
        y,x,path = dq.popleft()
        if y>=len(lines)-1:
             longest[len(lines)-2][len(lines[0])-1] = max(longest[len(lines)-2][len(lines[0])-1],len(path))
        elif y<=0 or longest[y][x]>=len(path) or (y,x) in path[:-1]:
            ...
        else:
            longest[y][x] = len(path)
            for d, yinc, xinc in ((0,-1,0),(1,0,1),(2,1,0),(3,0,-1)):
                ny = y + yinc
                nx = x + xinc
                if lines[ny][nx]=='.':
                        np = path[:]
                        np.append((ny,nx))
                        dq.append((ny,nx,np))
                elif lines[ny][nx] == slopedir[d]:
                    assert lines[ny+yinc][nx+xinc] == '.'
                    np=path[:]
                    np.append((ny,nx))
                    np.append((ny+yinc,nx+xinc))
                    dq.append((ny+yinc,nx+xinc,np,))

longest = [[0]*len(lines[0]) for _ in range(len(lines))]
solve(1,1)
print(longest[len(lines)-2][len(lines[0])-1])
