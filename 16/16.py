#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("16/in.raw", "r")
#f = open("16/sample.raw", "r")
lines = f.read().splitlines()

N,E,S,W = 0, 1, 2, 3
next_step=[(-1j),(1),(1j),(-1)]

def solve(beams):
    energized = [[['.']*4 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    ret=0
    while beams:
        p, direction = beams.popleft()
        y, x = int(p.imag), int(p.real)
        if 0 <= y <  len(lines) and 0 <= x < len(lines[0]):
            if energized[y][x][direction]=='.':
                    c = lines[y][x]
                    energized[y][x][direction]='#'
                    if (c == '|' and direction in [E,W]) or (c== '-' and direction in [N,S]):
                        for new_direction in [(direction + 1)%4 , (direction - 1)%4]:
                                beams.append((p+next_step[new_direction], new_direction))
                    elif (c == '/'):
                        if direction in [E,W]:
                                new_direction = (direction - 1)%4
                        else:
                                new_direction = (direction + 1)%4
                        beams.append((p+next_step[new_direction], new_direction))
                    elif c == '\\':
                        if direction in [E,W]:
                                new_direction = (direction + 1)%4
                        else:
                                new_direction = (direction - 1)%4
                        beams.append((p+next_step[new_direction], new_direction))
                    else:
                        beams.append((p+next_step[direction], direction))

    ret=0
    for energyline in energized:
        for energy in energyline:
                if any([e=='#' for e in energy]):
                    ret+=1
#                    print('#', end='')
                else:
#                    print('.',end='')
                    ...
 #       print()
    return(ret)


print(solve(deque([(0+0j,E)])))

# y, x, direction
res = 0
for x in range(len(lines[0])):
      res = max(res, solve(deque([(x+0j,S)])))
      res = max(res, solve(deque([(x+(len(lines)-1)*1j,N)])))
for y in range(len(lines)):
      res = max(res, solve(deque([(0+y*1j,E)])))
      res = max(res, solve(deque([((len(lines)-1)+y*1j,W)])))

print(res)

def print():
                for energyline in energized:
                    for energy in energyline:
                            if any([e=='#' for e in energy]):
                                print('#', end='')
                            else:
                                print('.',end='')
                    print()
