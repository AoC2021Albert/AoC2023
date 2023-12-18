#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("18/in.raw", "r")
#f = open("18/sample.raw", "r")
lines = f.read().splitlines()
pprint(lines)
H = len(lines)
L = len(lines[0])


U, R, D, L = 0, 1, 2, 3
DIR={
    'U' : U,
    'R' : R,
    'D' : D,
    'L' : L,    
}
next_step = [(-1j), (1), (1j), (-1)]

def solve1(lines):
    # Note: assuming clockwise
    area=0.0
    pos=0+0j
    direction=U
    for line in lines:
        new_direction, steps, color = line.split(' ')
        new_direction=DIR[new_direction]
        steps=int(steps)
        new_pos= pos+next_step[new_direction]*steps
        area += pos.real*new_pos.imag
        area -= pos.imag*new_pos.real
        if new_direction == (direction + 1) %4:
            area+=3/2
        else:
            area+=1/2
        area+=steps-1
        pos = new_pos
        direction = new_direction
    new_pos = 0+0j
    area += pos.real*new_pos.imag
    area -= pos.imag*new_pos.real
    area = area/2
    return(area)


def solve2(lines):
    # Note: assuming clockwise
    pos=0+0j
    direction=U
    area=1.0
    for line in lines:
        new_direction, steps, color = line.split(' ')
        color=color[2:-1]
        steps=int(color[:5],16)
        new_direction=int(color[-1])
        new_pos= pos+next_step[new_direction]*steps
        area += pos.real*new_pos.imag
        area -= pos.imag*new_pos.real
        if new_direction == (direction + 1) %4:
            area+=3/2
        else:
            area+=1/2
        area+=steps-1
        pos = new_pos
        direction = new_direction
    new_pos = 0+0j
    area += pos.real*new_pos.imag
    area -= pos.imag*new_pos.real
    area = area/2
    return(area)

print(solve1(lines))

print(solve2(lines))
