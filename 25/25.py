#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

f = open("25/in.raw", "r")
#f = open("25/sample.raw", "r")
lines = f.read().splitlines()

res = 0
edges = set()
destinations = defaultdict(list)
for i, line in enumerate(lines):
    left,right = line.split(': ')
    right=right.split(' ')
    for r in right:
        edges.add(tuple(sorted([left, r])))
        destinations[left].append(r)
        destinations[r].append(left)

'''
# remove all the edges that are loops
def remove_loops(unlooped, path, element):
    if element in path:
        loop = path[path.index(element):len(path)]+[element]
        for i in range(len(loop)-1):
            edge = (loop[i],loop[i+1]) if loop[i]>loop[i+1] else (loop[i+1],loop[i])
            if edge in unlooped:
                unlooped.remove(edge)
    else:
        for d in destinations[element]:
            edge=(element,d) if element>d else (d,element)
            if edge in unlooped and d!=path[-1]:
                remove_loops(unlooped, path+[element], d)

unlooped = deepcopy(edges)
for edge in edges:
    if edge in unlooped:
        remove_loops(unlooped,[edge[0]],edge[1])

# First attempts. Does not work. Would have only worked if there was a single connection between the two sub-graphs
#pprint(unlooped)


# Going to try with counting how many times an edge participates in the shortest path between nodes.
'''
# first we get the mininum distances, mindists
paths=[list(edge) for edge in edges]
mindists={edge:list(edge) for edge in edges}
while len(paths)>0:
    next_paths=list()
    for path in paths:
        src, mid = path[0],path[-1]
        for dst in destinations[mid]:
            if dst not in path:
                srcdst = tuple(sorted([src,dst]))
                if srcdst not in mindists:
                    mindists[srcdst]=path+[dst]
                    next_paths.append(path+[dst])
    paths = next_paths

#pprint(mindists)

uses=defaultdict(int)
for mindistpath in mindists.values():
    for node in range(len(mindistpath)-1):
        one, two = mindistpath[node], mindistpath[node+1]
        edge = (one,two) if one>two else (two,one)
        uses[edge]+=1

populated=[]
for k,v in uses.items():
    populated.append((v,k))

removal_candidates = sorted(populated,reverse=True)
#pprint(removal_candidates)
for a in range(2,len(removal_candidates)):
#    print(a)
    srca, dsta = sorted(removal_candidates[a][1])
    destinations[srca].remove(dsta)
    destinations[dsta].remove(srca)
    for b in range(1,a):
        srcb, dstb = sorted(removal_candidates[b][1])
        destinations[srcb].remove(dstb)
        destinations[dstb].remove(srcb)
        for c in range(0,b):
            srcc, dstc = sorted(removal_candidates[c][1])
            destinations[srcc].remove(dstc)
            destinations[dstc].remove(srcc)
            start = dstc
            visited=set([start])
            candidates = set(destinations[start])
            while candidates:
                new_candidates = set()
                for candidate in candidates:
                    if candidate not in visited:
                        visited.add(candidate)
                        new_candidates.update(destinations[candidate])
                candidates=new_candidates
            if len(visited)!=len(destinations):
                print((len(destinations)-len(visited)) * len(visited))
                exit()
            destinations[srcc].append(dstc)
            destinations[dstc].append(srcc)
        destinations[srcb].append(dstb)
        destinations[dstb].append(srcb)
    destinations[srca].append(dsta)
    destinations[dsta].append(srca)

print('FAIL')
