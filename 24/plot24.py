import matplotlib.pyplot as plt
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



ax = plt.figure().add_subplot(projection='3d')
delta_t = 2000000000000
vectors=[]
for hailstone in hailstones:
     p,v = hailstone
# Full lines
     vectors.append([[p[X],p[X]+delta_t*v[X]],[p[Y],p[Y]+delta_t*v[Y]],[p[Z],p[Z]+delta_t*v[Z]]])
# XY over Z=time
#     vectors.append([[p[X],p[X]+delta_t*v[X]],[p[Y],p[Y]+delta_t*v[Y]],[0,delta_t]])
# X over Y = time
#     vectors.append([[p[X],p[X]+delta_t*v[X]],[0,delta_t],[0,0]])
pprint(vectors)
for vector in vectors:
      ax.plot(vector[0], vector[1], zs=vector[2])

plt.show()



