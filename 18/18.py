#!/usr/bin/env python
f = open("18/in.raw", "r")
# f = open("18/sample.raw", "r")
lines = f.read().splitlines()
DIR = 'RDLU'
next_step = [(1), (1j), (-1), (-1j)]


def get_data1(line):
    direction, steps, _ = line.split(' ')
    direction = DIR.find(direction)
    steps = int(steps)
    return (direction, steps)


def get_data2(line):
    hex_digits = line.split(' ')[-1][2:-1]
    steps = int(hex_digits[:5], 16)
    direction = int(hex_digits[-1])
    return (direction, steps)


def solve(lines, get_data):
    # Note: assuming clockwise
    # https://en.wikipedia.org/wiki/Shoelace_formula for area
    area = 0.0
    pos = 0+0j
    for line in lines:
        direction, steps = get_data(line)
        new_pos = pos+next_step[direction] * steps
        area += pos.real * new_pos.imag
        area -= pos.imag * new_pos.real
        # Add border area (will be divided by 2)
        area += steps
        pos = new_pos
    new_pos = 0+0j
    area += pos.real * new_pos.imag
    area -= pos.imag * new_pos.real
    area = area / 2 + 1
    return (int(area))


print(solve(lines, get_data1))
print(solve(lines, get_data2))
