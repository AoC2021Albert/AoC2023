#!/usr/bin/env python
f = open("10/in.raw", "r")
lines = f.read().splitlines()

N, E, S, W = (0, 1, 2, 3)

# We use complex numbers, with the imaginary part (j in python) being the Y coordinate
#               N     E    S      W
DIRECTIONS = [(-1j), (1), (1j), (-1)]
# Next direction given previous direction
NEXT_DIR = [{'|': N, 'F': E, '7': W}, # Previous N
            {'-': E, '7': S, 'J': N}, # Previous E
            {'|': S, 'J': W, 'L': E}, # Previous S
            {'-': W, 'L': N, 'F': S}] # Previous W

def char_at(lines, pos):
    return (lines[int(pos.imag)][int(pos.real)])

# Find starting position (aka 'S', s_pos)
s_pos = [x+y*1j for y, line in enumerate(lines) if line.find('S') != -1
                for x, c in enumerate(line) if c == 'S'][0]

# Now find one neighbour pointing towards us
dir = N
while char_at(lines, s_pos+DIRECTIONS[dir]) not in NEXT_DIR[dir]:
    dir += 1
pos = s_pos + DIRECTIONS[dir]

step = 1
# https://en.wikipedia.org/wiki/Shoelace_formula
area = s_pos.real*pos.imag - s_pos.imag*pos.real
while pos != s_pos:
    dir = NEXT_DIR[dir][char_at(lines, pos)]
    new_pos = pos + DIRECTIONS[dir]
    area += pos.real*new_pos.imag
    area -= pos.imag*new_pos.real
    pos = new_pos
    step += 1
area = area/2

print(f'Part 1 answer: {step/2}')
# https://en.wikipedia.org/wiki/Pick%27s_theorem
print(f'Part 2 answer: {area-(step/2)+1}')
