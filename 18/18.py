#!/usr/bin/env python
f = open("18/in.raw", "r")
#f = open("18/sample.raw", "r")
lines = f.read().splitlines()
U, R, D, L = 0, 1, 2, 3
DIR = {
    'R': R,
    'D': D,
    'L': L,
    'U': U,
}
next_step = [(1), (1j), (-1), (-1j)]


def get_data1(line):
    direction, steps, _ = line.split(' ')
    direction = DIR[direction]
    steps = int(steps)
    return (direction, steps)


def get_data2(line):
    hex_digits = line.split(' ')[-1][2:-1]
    steps = int(hex_digits[:5], 16)
    direction = int(hex_digits[-1])
    # Note: directions don't match
    return (direction, steps)


def solve(lines, get_data):
    # Note: assuming clockwise
    area = 0.0
    pos = 0+0j
    direction, steps = get_data(lines[-1])  # Direction of last
    for line in lines:
        new_direction, steps = get_data(line)
        new_pos = pos+next_step[new_direction] * steps
        area += pos.real * new_pos.imag
        area -= pos.imag * new_pos.real
        if new_direction == (direction + 1) % 4:
            area += 3/2
        else:
            area += 1/2
        area += steps - 1
        pos = new_pos
        direction = new_direction
    new_pos = 0+0j
    area += pos.real * new_pos.imag
    area -= pos.imag * new_pos.real
    area = area / 2
    return (int(area))


print(solve(lines, get_data1))
print(solve(lines, get_data2))
