#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy

f = open("21/in.raw", "r")
#f = open("21/sample.raw", "r")
lines = f.read().splitlines()

next_step=(-1j,1,1j,-1)
lines=["#"*(len(lines[0])+2)]+["#"+line+"#" for line in lines]+["#"*(len(lines[0])+2)]
res=0

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'S':
            poss = set([x+y*1j])

total_poss=deepcopy(poss)
for loop in range(64):
    new_poss = set()
    for pos in poss:
        for direction in range(4):
            np = pos+next_step[direction]
            if lines[int(np.imag)][int(np.real)] == ".":
                new_poss.add(np)
    total_poss=total_poss.union(new_poss)
    poss = new_poss

print(len(poss))



print(res)