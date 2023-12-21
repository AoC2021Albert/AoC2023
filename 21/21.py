#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy


# Third, go for the real thing, "in.raw"
FILE="21/in.raw"
REPETITIONS = 202300
DO_N = False

# Second try "mysample.raw" without DO_N, should give the same result as first try
#FILE = "21/mysample.raw"
#REPETITIONS = 4
#DO_N = False

# First try "mysample.raw" with DO_N
# FILE = "21/mysample.raw"
# REPETITIONS = 4
# DO_N = True

# Set to false to not print the maps
DISPLAY = True

f = open(FILE, "r")
lines = f.read().splitlines()
next_step=((-1,0),(0,1),(1,0),(0,-1))
YLENORIG=YLEN=len(lines)
XLENORIG=XLEN=len(lines[0])

def printat (y, x, c):
    print("\033[%d;%dH%c" % (y+2, (x+2)*2, c))

def clearscrean():
    print("\033[2J")


N_UPLICATE = 2*REPETITIONS+1 if DO_N else 1
new_lines = []
for y in range(len(lines)*N_UPLICATE):
    new_line = []
    for x in range(len(lines[0])*N_UPLICATE):
        c=lines[y%YLEN][x%XLEN]
        if c == "S":
            c="."
        new_line.append(c)
    new_lines.append(new_line)

lines = new_lines
YLEN=len(lines)
XLEN=len(lines[0])


nmap=[]
for y, line in enumerate(lines):
    nline = []
    for x, c in enumerate(line):
        neighs = []
        if c in [".","S"]:
            for direction in range(4):
                ny = y + next_step[direction][0]
                nx = x + next_step[direction][1]
                if 0 <= nx < len(lines[0]) and 0<=ny<len(lines):
                    if lines[ny][nx] in [".","S"]:
                        neighs.append((ny,nx))
        nline.append(tuple(neighs))
    nmap.append(nline)

# Set VERY tiny font if you want to see the in.raw
def print_map(uses):
    if not DISPLAY:
        return()
    for y in range(len(uses)):#//2+1):
        for x in range(len(uses[0])):
            if lines[y][x] == "#":
                assert uses[y][x]==0
                printat(y+y//YLENORIG,x+x//YLENORIG,'#')
            else:
              printat(y+y//YLENORIG,x+x//YLENORIG,str(uses[y][x]))

def get_data(uses):
    new_uses = [[0] * len(lines[0]) for _ in range(len(lines))]

    data = ['INITIAL'] # So that data[64] becomes data after 64 steps taken
    old_on = [0,0]
    for loop in range(10000):
        for y, nline in enumerate(nmap):
            for x, c in enumerate(nline):
                for n in c:
                    new_uses[y][x] = 1 if uses[n[0]][n[1]]==1 else new_uses[y][x]
        uses, new_uses = new_uses, uses
        on = sum([sum(v for v in line) for line in uses])
        if old_on[loop%2] == on:
            print_map(uses)
            print()
            print(on)
            return(data)
        data.append(on)
        print_map(uses)
        print(on)
        print(len(data))
        print(loop)
        #input()
        #print(loop,on)
        old_on[loop%2] = on
    print('FAIL')
    exit()

BOTTOM_ENTRY = (YLEN-1, XLEN // 2)
LEFT_ENTRY   = (YLEN//2,  0)
TOP_ENTRY    = (  0, XLEN//2)
RIGHT_ENTRY  = (YLEN//2,XLEN-1)
BOTTOM_LEFT_ENTRY = (YLEN-1,0)
LEFT_TOP_ENTRY = (0,0)
TOP_RIGHT_ENTRY = (0, XLEN-1)
RIGHT_BOTTOM_ENTRY = (YLEN-1, XLEN-1)

clearscrean()
datas=[]
for entry_points in  (# ((YLEN//2,XLEN//2),),):
    ((YLEN//2,XLEN//2),), # Initial
    (BOTTOM_ENTRY,),
    (LEFT_ENTRY,),
    (TOP_ENTRY,),
    (RIGHT_ENTRY,),
    (BOTTOM_LEFT_ENTRY,),
    (LEFT_TOP_ENTRY,),
    (TOP_RIGHT_ENTRY,),
    (RIGHT_BOTTOM_ENTRY,),
    ):
    uses = [[0]*len(lines[0]) for _ in range(len(lines))]
    for y,x in entry_points:
        uses[y][x] = 1
    datas.append(get_data(uses))
    print(len(datas[-1]),datas[-1][-4:])

print(YLEN//2)
if DO_N:
    print(datas[0][YLEN//2])
    exit()

WIDTH = YLEN
OFFSET = (YLEN-1) // 2
loops = WIDTH*REPETITIONS+OFFSET

central_radius = YLEN//2
print(f'central_radius: {central_radius}')
out_of_central = (loops - central_radius)
print(f'out_of_central: {out_of_central}')
fully_traversed_out = out_of_central // YLEN
print(f'fully_traversed_out: {fully_traversed_out}')
print(f'CHECKSUM: {fully_traversed_out*YLEN+central_radius} == {loops}')


print(datas[0][-2],1,"CENTER") #44??
result  = datas[0][-2] #44??
print(datas[1][YLEN-1],1,"BOTTOM") # One corner
result += datas[1][YLEN-1] # One corner
print(datas[2][YLEN-1],1,"LEFT") # One corner
result += datas[2][YLEN-1] # One corner
print(datas[3][YLEN-1],1,"TOP") # One corner
result += datas[3][YLEN-1] # One corner
print(datas[4][YLEN-1],1,"RIGHT") # One corner
result += datas[4][YLEN-1] # One corner

print(datas[5][YLEN+OFFSET-1] , (REPETITIONS - 1), "Long corner bottom left")
result += datas[5][YLEN+OFFSET-1] * (REPETITIONS - 1)
print(datas[5][OFFSET-1] , REPETITIONS, "Short corner bottom left")
result += datas[5][OFFSET-1] * REPETITIONS
print(datas[6][YLEN+OFFSET-1] , (REPETITIONS - 1), "Long corner left top")
result += datas[6][YLEN+OFFSET-1] * (REPETITIONS - 1)
print(datas[6][OFFSET-1] , REPETITIONS, "Short corner left top")
result += datas[6][OFFSET-1] * REPETITIONS
print(datas[7][YLEN+OFFSET-1] , (REPETITIONS - 1), "Long corner top right")
result += datas[7][YLEN+OFFSET-1] * (REPETITIONS - 1)
print(datas[7][OFFSET-1] , REPETITIONS, "short corner top right")
result += datas[7][OFFSET-1] * REPETITIONS
print(datas[8][YLEN+OFFSET-1] , (REPETITIONS - 1), "Long corner right bottom")
result += datas[8][YLEN+OFFSET-1] * (REPETITIONS - 1)
print(datas[8][OFFSET-1] , REPETITIONS, "Short corner right bottom")
result += datas[8][OFFSET-1] * REPETITIONS

full_rings = REPETITIONS - 1
fulls = ((full_rings * (full_rings + 1) ) / 2 ) * 4
odd_rings = full_rings // 2
fulls_at_odd =  ((odd_rings * (odd_rings + 1) ) / 2 ) * 8
fulls_at_even = fulls - fulls_at_odd
print(datas[0][-2] , fulls_at_odd, "fulls at odds")
result += datas[0][-2] * fulls_at_odd
print(datas[0][-1] , fulls_at_even, "fulls at even")
result += datas[0][-1] * fulls_at_even
print(result)