#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("17/in.raw", "r")
#f = open("17/sample.raw", "r")
lines = [list(map(int, [c for c in line])) for line in f.read().splitlines()]
pprint(lines)
H = len(lines)
L = len(lines[0])

N, E, S, W = 0, 1, 2, 3
next_step = [(-1j), (1), (1j), (-1)]


def solve(map, paths):
    min_maps = [[[999999999999]*4*3 for _ in range(len(map[0]))]
                for _ in range(len(map))]
    ret = [999999999999] * 4 * 3
    while paths:
        p, direction, steps_left, cost = paths.popleft()
        y, x = int(p.imag), int(p.real)
        if min_maps[y][x][direction*3+steps_left] > cost:
            min_maps[y][x][direction*3+steps_left] = cost
            if y == H - 1 and x == L - 1:
                ret[direction*3 +
                    steps_left] = min(ret[direction*3+steps_left], cost)
            else:
                for new_direction in [N, E, S, W]:
                    if new_direction == ((direction + 2) % 4):
                        # Can't go back
                        ...
                    elif new_direction == direction and steps_left == 0:
                        # Cant' continue further
                        ...
                    else:
                        new_p = p + next_step[new_direction]
                        new_y, new_x = int(new_p.imag), int(new_p.real)
                        if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
                            if new_direction == direction:
                                new_steps_left = steps_left - 1
                            else:
                                new_steps_left = 2
                            new_cost = cost + map[new_y][new_x]
                            paths.append(
                                (new_p, new_direction, new_steps_left, new_cost))
    return (min(ret))


print(solve(lines, deque([(0+0j, E, 2, 0), (0+0j, S, 2, 0)])))
exit()
# y, x, direction
res = 0
for x in range(len(lines[0])):
    res = max(res, solve(deque([(x+0j, S)])))
    res = max(res, solve(deque([(x+(len(lines)-1)*1j, N)])))
for y in range(len(lines)):
    res = max(res, solve(deque([(0+y*1j, E)])))
    res = max(res, solve(deque([((len(lines)-1)+y*1j, W)])))

print(res)


def print():
    for energyline in energized:
        for energy in energyline:
            if any([e == '#' for e in energy]):
                print('#', end='')
            else:
                print('.', end='')
        print()
