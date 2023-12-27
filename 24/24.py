#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from sympy import Symbol, solve_poly_system


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
        print('paralel:', h1, h2)
        print(hailstones[h1])
        print(hailstones[h2])
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

# Part 2
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
vx = Symbol('vx')
vy = Symbol('vy')
vz = Symbol('vz')

eqs = []
ts = []

for i, hs in enumerate(hailstones[:3]):
  x0,y0,z0 = hs[0]
  xv,yv,zv = hs[1]
  t = Symbol('t'+str(i))
  eqx = x + vx*t - x0 - xv*t
  eqy = y + vy*t - y0 - yv*t
  eqz = z + vz*t - z0 - zv*t

  eqs.append(eqx)
  eqs.append(eqy)
  eqs.append(eqz)
  ts.append(t)

# https://docs.sympy.org/latest/modules/solvers/solvers.html#systems-of-polynomial-equations
result = solve_poly_system(eqs,x,y,z,vx,vy,vz,ts[0],ts[1],ts[2])
print(sum(result[0][:3]))
