#!/usr/bin/env python


f = open("2/in.raw", "r")
lines = f.read().splitlines()

res = 0

LIMITS = {"red": 12,
          "green": 13,
          "blue": 14}
l = 1
for line in lines:
    line = line.split(': ')[1]
    valid = True
    for round in line.split('; '):
        for balls in round.split(', '):
            number, color = balls.split(' ')
            if int(number) > LIMITS[color]:
                valid = False
    if valid:
        res += l
    l += 1
print(res)

res = 0
for line in lines:
    line = line.split(': ')[1]
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0}
    for round in line.split('; '):
        for balls in round.split(', '):
            number, color = balls.split(' ')
            number = int(number)
            min_cubes[color] = max(min_cubes[color], number)
    res += min_cubes['blue'] * min_cubes['green']*min_cubes['red']
print(res)
