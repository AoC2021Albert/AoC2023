#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("23/in.raw", "r")
f = open("23/sample.raw", "r")
lines = f.read().splitlines()
res = 0
y,x=0,1
fy=len(lines)-1

DIRS=((-1,0),(0,1),(1,0),(0,-1))

SRCFORK = (0,1)
DESTFORK = (len(lines)-1,len(lines[-1])-2)
# find_forks
forks={SRCFORK: [2],
       DESTFORK: [0]}
for y in range(1,len(lines)-1):
     for x in range(1,len(lines[0])-1):
          if lines[y][x]!='#':
              dirs = []
              for d in range(4):
                   yinc, xinc = DIRS[d]
                   if lines[y+yinc][x+xinc] != '#':
                        dirs.append(d)
              if len(dirs)>2:
                   forks[(y,x)]=dirs
              else:
                   assert len(dirs)==2

def find_neigh_paths(fork):
     y,x = fork
     dirs = forks[fork]
     ret=[]
     for d in dirs:
        dist = 1
        ny, nx = y, x
        yinc, xinc = DIRS[d]
        nd = (d - 1)%4
        while (ny+yinc,nx+xinc) not in forks.keys():
             ny += yinc
             nx += xinc
             while lines[ny+DIRS[nd][0]][nx+DIRS[nd][1]] == '#':
                  nd = (nd+1)%4
             yinc, xinc = DIRS[nd]
             nd = (nd -1)%4
             dist+=1
        ret.append(((ny+yinc,nx+xinc),dist))
     return(ret)


# find distance between forks
dests = {}
for fork in forks:
     dests[fork] = find_neigh_paths(fork)

longest_path=0
# find longest path
def take_all_paths(fork, path, pathlen):
     global longest_path
     if fork in path:
          return()
     else:
          path.append(fork)
          if fork==DESTFORK:
               pprint(pathlen)
               pprint(path)
               longest_path = max(longest_path,pathlen)
          else:
               for subfork, dist in dests[fork]:
                    take_all_paths(subfork, path, pathlen+dist)
          path.pop()

take_all_paths(SRCFORK,[],0)
print(longest_path)