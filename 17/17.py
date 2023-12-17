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
    min_maps = [[[999999999999]*4*7 for _ in range(len(map[0]))]
                for _ in range(len(map))]
    ret = [999999999999] * 4 * 7
    while paths:
        p, direction, steps_left, cost = paths.popleft()
        y, x = int(p.imag), int(p.real)
        if min_maps[y][x][direction*7+steps_left] > cost:
            min_maps[y][x][direction*7+steps_left] = cost
            if y == H - 1 and x == L - 1:
                ret[direction*7 +
                    steps_left] = min(ret[direction*7+steps_left], cost)
            else:
                for new_direction in [N, E, S, W]:
                    if new_direction == ((direction + 2) % 4):
                        # Can't go back
                        ...
                    elif new_direction == direction and steps_left == 0:
                        # Cant' continue further
                        ...
                    else:
                        if new_direction == direction:
                            new_steps_left = steps_left - 1
                            new_p = p + next_step[new_direction]
                            new_y, new_x = int(new_p.imag), int(new_p.real)
                            if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
                                new_cost = cost + map[new_y][new_x]
                        else:
                            new_steps_left = 6
                            new_p = p + next_step[new_direction]
                            new_y, new_x = int(new_p.imag), int(new_p.real)
                            if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
                                new_cost = cost + map[new_y][new_x]
                            for _ in range(3):
                                new_p = new_p + next_step[new_direction]
                                new_y, new_x = int(new_p.imag), int(new_p.real)
                                if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
                                    new_cost = new_cost + map[new_y][new_x]
                                else:
                                    break
                        if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
                            paths.append(
                                (new_p, new_direction, new_steps_left, new_cost))
    return (min(ret))


print(solve(lines, deque([(0+0j, E, 2, 0), (0+0j, S, 2, 0)])))
