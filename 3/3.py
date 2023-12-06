#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

f = open("3/in.raw", "r")
lines = f.read().splitlines()

for l in range(len(lines)):
    lines[l] = '.'+lines[l]+'.'
lines = ['.'*len(lines[0])]+lines+['.'*len(lines[0])]

DIR = [[-1, -1], [-1, 0], [-1, 1],
       [ 0, -1],          [ 0, 1],
       [ 1, -1], [ 1, 0], [ 1, 1]]

res = 0
for l, line in enumerate(lines):
    n = 0
    touches = False
    for c, ch in enumerate(line):
        if ch.isdigit():
            n = n*10+int(ch)
            for y, x in DIR:
                neighbour = lines[l+y][c+x]
                if not (neighbour.isdigit() or neighbour == '.'):
                    touches = True
        else:
            # end of number
            if touches:
                res += n
            n = 0
            touches = False
print(res)


res = 0
all_touches = defaultdict(list)

for l, line in enumerate(lines):
    print(line)
    n = 0
    my_touches = set()
    for c, ch in enumerate(line):
        if ch.isdigit():
            n = n*10+int(ch)
            for y, x in DIR:
                neighbour = lines[l+y][c+x]
                if neighbour == '*':
                    my_touches.add((l+y, c+x))
        else:
            # end of number
            for touch in my_touches:
                all_touches[touch].append(n)
            n = 0
            my_touches = set()

pprint(all_touches)
for pos, gear in all_touches.items():
    if len(gear) == 2:
        v = gear[0]*gear[1]
        print(f'Gear at {pos}, with value {v}')
        res += v

print(res)
