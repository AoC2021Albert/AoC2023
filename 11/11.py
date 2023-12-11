#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("11/in.raw", "r")
#f = open("11/sample.raw", "r")
lines = f.read().splitlines()

EXPANSE=999999

def star_distance(map, EXPANSE):
    ret=0
    offsetcols=[0]*len(map[0])
    offsetrows=[0]*len(map)
    emptycols=[True]*len(map[0])
    # Scan de map row by row
    for y, row in enumerate(map):
        # If no stars in row
        if row.find('#')==-1:
            # Add EXPANSE offset to subsequent rows
            for i in range(y+1,len(map)):
               offsetrows[i]+=EXPANSE
        # Detect Columns that have stars on this row
        for x, c in enumerate(row):
            if c == '#':
                emptycols[x]=False

    # For each column
    for x, is_empty in enumerate(emptycols):
        if is_empty:
            # Add EXPANSE offset to subsecuent columns
            for i in range(x+1,len(map[0])):
                offsetcols[i]+=EXPANSE

    # With offsetcols and offsetrows ready
    # find real position of stars
    stars = []
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if row[x]=='#':
                stars.append((y+offsetrows[y],x+offsetcols[x]))

    # The distance is the X-distance + Y-distance
    # For each star
    for i, star in enumerate(stars):
        # Check distance to subsequent stars
        for j in range(i+1,len(stars)):
            ret+=abs(star[0]-stars[j][0])
            ret+=abs(star[1]-stars[j][1])

    return(ret)

print(f'Part 1: {star_distance(lines,1)}')
print(f'Part 2: {star_distance(lines,999999)}')
