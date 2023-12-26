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
# f = open("25/sample.raw", "r")
lines = f.read().splitlines()

res = 0
destinations = defaultdict(list)
for i, line in enumerate(lines):
    left, right = line.split(': ')
    right = right.split(' ')
    for r in right:
        destinations[left].append(r)
        destinations[r].append(left)
# to_sample can be ANY node, we just need one, we get the last 'left'
sample_node = left

# edge_visits dictionary
#    Key   = edge (identified by a tuple of both nodes, sorted min,max )
#    Value = number of visits the edge has on all min-paths from any node to any node
# The idea is that most visited edges have better chances of being one of the three
# that "connect" both sub-graphs.
edge_visits = defaultdict(int)
# We count min_paths from each starting node to each destination node
# This will count things twice, as we record both a->b->c and c->b->a
# although it might use different paths in one direction and the other.
# The path on the return of the given example might be c->d->a
# But this is not relevant to us. We just want edges with most passes
# to optimize "brute force" search
for src, dsts in destinations.items():
    visited = set([src])
    paths = deque()
    for dst in dsts:
        # The elements of the path are optimized for computin use of edges
        # So a path will be ((edge,node,),(edge,node,),(edge,node,),)
        # example, the path str->mid-lst will be represented as
        # (('mid','str','mid'),('lst','mid','lst',))
        # The first two values represent the edge, the last value is the
        # last node in the path.
        paths.append(((min(src, dst), max(src, dst), dst,),))
        visited.add(dst)
    while len(paths) > 0:
        path = paths.popleft()
        lastnode = path[-1][-1]
        for dstnode in destinations[lastnode]:
            if dstnode not in visited:
                visited.add(dstnode)
                newpath = path + \
                    ((min(lastnode, dstnode), max(lastnode, dstnode), dstnode,),)
                for edge in newpath:
                    edge_visits[(edge[0], edge[1],)] += 1
                paths.append(newpath)


def remove(destinations, to_remove):
    for src, dst in to_remove:
        destinations[src].remove(dst)
        destinations[dst].remove(src)


def readd(destinations, to_remove):
    for src, dst in to_remove:
        destinations[src].append(dst)
        destinations[dst].append(src)


def count_set(destintions, sample_node):
    start = sample_node
    visited = set([start])
    candidates = set(destinations[start])
    while candidates:
        new_candidates = set()
        for candidate in candidates:
            if candidate not in visited:
                visited.add(candidate)
                new_candidates.update(destinations[candidate])
        candidates = new_candidates
    return (len(visited))


removal_candidates = sorted(edge_visits.items(), key=lambda x: -x[1])
to_remove = []
for a in range(2, len(removal_candidates)):
    to_remove.append(removal_candidates[a][0])
    for b in range(1, a):
        to_remove.append(removal_candidates[b][0])
        for c in range(0, b):
            to_remove.append(removal_candidates[c][0])
            remove(destinations, to_remove)
            set_size = count_set(destinations, sample_node)
            if set_size != len(destinations):
                print((len(destinations)-set_size) * set_size)
                exit()
            readd(destinations, to_remove)
print('FAIL')
