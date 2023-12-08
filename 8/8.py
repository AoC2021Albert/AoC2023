#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

# f = open("8/sample2.raw", "r")
f = open("8/in.raw", "r")
lines = f.read().splitlines()

turns = lines[0]
res = 0
map = dict()
for i in range(2, len(lines)):
    src, dst = lines[i].split(' = ')
    dstl, dstr = dst[1:-1].split(', ')
    map[src] = (dstl, dstr)
pos = 'AAA'
while pos != 'ZZZ':
    turn = 0 if turns[res % len(turns)] == 'L' else 1
    pos = map[pos][turn]
    res += 1
    # print(turn,pos)
print(res)

multipliers = []
for start in [p for p in map.keys() if p[-1] == 'A']:
    res = 0
    firstZ = None
    lastZ = None
    allZ = []
    pos = start
    while firstZ is None or lastZ != firstZ:
        turn = 0 if turns[res % len(turns)] == 'L' else 1
        pos = map[pos][turn]
        if pos[-1] == 'Z':
            if firstZ is None:
                firstZ = (pos, res % len(turns))
            else:
                lastZ = (pos, res % len(turns))
            allZ.append((pos, res+1))
        res += 1
    print(f'{start} has {allZ} after {res} moves')
    multipliers.append(allZ[0][1])
# note: turns out that all "node-A" just find a single "node-Z"
# This would not work if there was more than one "node-Z" per "node-A"
print(math.lcm(*multipliers))
