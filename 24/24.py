#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("24/in.raw", "r")
LOW =200000000000000
HIGH=400000000000000

'''f = open("24/sample.raw", "r")
LOW = 7
HIGH=27
'''
X,Y,Z=0,1,2
P,V=0,1

lines = f.read().splitlines()
hailstones = []
line_eq = []
for line in lines:
    p,v=line.split(' @ ')
    p=tuple(map(int,p.split(', ')))
    v=tuple(map(int,v.split(', ')))
    hailstones.append((p,v))
    const = p[Y] - (v[Y]*p[X]/v[X])
    slope = v[Y]/v[X]
    line_eq.append((slope, const))

sign=lambda x: math.copysign(1,x)

def timeatx(x, h):
    hs = hailstones[h]
    return((x-hs[P][X])/hs[V][X])

def intersect_line_eq(h1, h2):
    le1=line_eq[h1]
    le2=line_eq[h2]
    a = le1[0]
    c = le1[1]
    b = le2[0]
    d = le2[1]
    if a == b:
        if c == d:
            print('OVERLAPPING')
            pprint(le1, le2)
        return(False) # paralel
    else:
        x = (d-c)/(a-b)
        y = a*(d-c)/(a-b) + c
        return( (
                LOW <= x <= HIGH
            ) and (
                LOW <= y <= HIGH
            ) and (
                timeatx(x, h1) >= 0
            ) and(
                timeatx(x, h2) >= 0
            ))


lh=len(hailstones)
res=0
for h1 in range(lh):
    for h2 in range(h1+1,lh):
        if intersect_line_eq(h1, h2):
            res+=1
print(res)

exit()



def intersect2d(h1, h2):
    x1,y1,z1=h1[0]
    vx1,vy1,vz1=h1[1]
    x2,y2,z2=h2[0]
    vx2,vy2,vz2=h2[1]
    slope1 = vy1 / vx1
    slope2 = vy2 / vx2
    if slope1 == slope2:
        return(0) #assuming no two hailstones will have same path (even delayed in time or with different speeds)

lh=len(hailstones)
res=0
for h1 in range(lh):
    x1,y1,z1=hailstones[h1][0]
    vx1,vy1,vz1=hailstones[h1][1]
    # put x just before LOW
    for h2 in range(h1+1,lh):
        x2,y2,z2=h2[0]
        vx2,vy2,vz2=h2[1]
        res += intersect2d(hailstones[h1], hailstones[h2])
