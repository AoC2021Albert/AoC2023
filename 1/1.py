#!/usr/bin/env python


f = open("1/in.raw", "r")
lines = f.read().splitlines()

res = 0

for line in lines:
    i = 0
    firstd = -1
    lastd = -1
    while i < len(line):
        i += 1
        l = line[:i]
        if l[-1].isdigit():
            firstd = int(l[-1]) if firstd == -1 else firstd
            lastd = int(l[-1])
        else:
            for n, number in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if len(number) <= len(l) and l[-len(number):] == number:
                    firstd = n + 1 if firstd == -1 else firstd
                    lastd = n + 1
    print(firstd*10 + lastd)
    res += firstd*10 + lastd

print("part2", res)
