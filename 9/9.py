#!/usr/bin/env python
from pprint import pprint

f = open("9/in.raw", "r")
#f = open("9/sample.raw", "r")
lines = f.read().splitlines()
# part 1 as done at the moment
res = 0
for line in lines:
    seq = []
    seq.append(list(map(int, line.split(' '))))
    depth = 0
    while seq[-1][-1] != 0:
        seq.append(list(seq[-1][i+1]-seq[-1][i]
                   for i in range(len(seq[-1])-1)))
    last = 0
    while seq:
        s = seq.pop()
        last += s[-1]
    #pprint(s)
    #print(last)
    res += last
print(res)

#Part 2 as done at the moment
res = 0
for line in lines:
    seq = []
    seq.append(list(map(int, line.split(' '))))
    depth = 0
    while seq[-1][-1] != 0:
        seq.append(list(-seq[-1][i+1]+seq[-1][i]
                   for i in range(len(seq[-1])-1)))
    last = 0
    while seq:
        s = seq.pop()
        s.reverse()
        last += s[-1]
    #pprint(s)
    #print(last)
    res += last
print(res)

#Part 1 and 2 at once (simpler)
res1 = 0
res2 = 0
for line in lines:
    seq = []
    seq.append(list(map(int, line.split(' '))))
    depth = 0
    while seq[-1][-1] != 0:
        seq.append(list(seq[-1][i+1]-seq[-1][i]
                   for i in range(len(seq[-1])-1)))
    last = 0
    first = 0
    while seq:
        s = seq.pop()
        last += s[-1]
        first = s[0] - first
    #pprint(s)
    #print(last)
    res1 += last
    res2 += first
print(res1)
print(res2)
