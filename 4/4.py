#!/usr/bin/env python
import re

f = open("4/in.raw", "r")
lines = f.read().splitlines()

p1 = 0

amount = [1]*len(lines)
for l, line in enumerate(lines):
    line = re.split(': *', line)[1]
    t = re.split(' *\| *', line)
    winl, minel = t
    win = set(re.split('  *', winl))
    mine = set(re.split('  *', minel))
    common = win.intersection(mine)
    if common:
        for k in range(l+1, l+1+len(common)):
            amount[k] += amount[l]
        p1 = p1 + 2**(len(common)-1)

print(p1)
print(sum(amount))
