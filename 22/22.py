#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("22/in.raw", "r")
#f = open("22/sample.raw", "r")
lines = f.read().splitlines()

X, Y, Z = 0,1,2

bricks = []
for i, line in enumerate(lines):
    p1, p2 = line.split('~')
    p1 = list(map(int,p1.split(',')))
    p2 = list(map(int,p2.split(',')))
    for d in range(3):
        assert p1[d] <= p2[d]
    test  = 0 if p1[Z]==p2[Z] else 1
    test += 0 if p1[X]==p2[X] else 1
    test += 0 if p1[Y]==p2[Y] else 1
    assert test<=1
    bricks.append((p1[Z], p2[Z],p1[X], p2[X], p1[Y], p2[Y]))

space = [[[None] * 10 for _ in range(10)] for _ in range(320)]
highest = [[0] * 10 for _ in range(10)]

restonme = {}
restedby = {}
for brick in sorted(bricks):
    zi, zf, xi, xf, yi, yf = brick
    zbase = 0
    for x in range(xi, xf+1):
        for y in range(yi, yf+1):
            zbase = max(zbase, highest[x][y])
    zdesc = zi - zbase
    zi -= zdesc
    zf -= zdesc
    restonme[brick] = set()
    restedby[brick] = set()
    for z in range(zi, zf+1):
        for x in range(xi, xf+1):
            for y in range(yi, yf+1):
                space[z][x][y] = brick
                highest[x][y] = zf + 1
                if underbrick := space[z-1][x][y]:
                    if underbrick != brick:
                        restedby[brick].add(underbrick)
                        restonme[underbrick].add(brick)

p1 = 0
for basebrick, dependantbriks in restonme.items():
    canremove = True
    for brik in dependantbriks:
        canremove = canremove and len(restedby[brik])>1
    if canremove:
        pprint(basebrick)
        p1 += 1
print(p1)