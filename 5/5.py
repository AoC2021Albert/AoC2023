#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re

# f = open("5/sample.raw", "r")
f = open("5/in.raw", "r")
lines = f.read().splitlines()

res = 0
seeds = set(map(int, lines[0].split(': ')[1].split(' ')))

l = 2
while l < len(lines):
    src, dst = lines[l].split(' ')[0].split('-to-')
    print(f'Mapping {src} to {dst}')
    l += 1
    oldseeds = seeds
    seeds = set()
    while l < len(lines) and lines[l]:
        dstl, srcl, length = map(int, lines[l].split(' '))
        print(dstl, srcl, length)
        pendingseeds = set(oldseeds)
        for seed in oldseeds:
            if (seed >= srcl) and (seed < srcl + length):
                pendingseeds.remove(seed)
                seeds.add(seed-srcl+dstl)
        oldseeds = pendingseeds
        l += 1
    seeds.update(oldseeds)
    pprint(seeds)
    l += 1
print(min(seeds))

print()
print()

seeds = []
numl = list(map(int, lines[0].split(': ')[1].split(' ')))
for i in range(len(numl)//2):
    seeds.append((numl[i*2], numl[i*2+1]))

pprint(seeds)
l = 2
while l < len(lines):
    src, dst = lines[l].split(' ')[0].split('-to-')
    print(f'Mapping {src} to {dst}')
    l += 1
    oldseeds = seeds
    seeds = []
    while l < len(lines) and lines[l]:
        dstl, srcl, length = map(int, lines[l].split(' '))
        # print(dstl, srcl, length)
        pendingseeds = oldseeds[:]
        for seed in oldseeds:
            seed_src = seed[0]
            seed_len = seed[1]
            if seed_src < srcl:
                # Sx
                if seed_src + seed_len - 1 >= srcl:
                    if seed_src + seed_len - 1 > srcl + length - 1:
                        # SB
                        pendingseeds.remove(seed)
                        # Add back the "head"
                        pendingseeds.append((seed_src, srcl - seed_src))
                        # Add back the "tail"
                        pendingseeds.append(
                            (srcl+length, seed_src+seed_len - (srcl+length)))
                        # Transpose the complete "center"
                        seeds.append((dstl, length))
                    else:
                        # SM
                        pendingseeds.remove(seed)
                        # Add back the "head"
                        pendingseeds.append((seed_src, srcl - seed_src))
                        # transpose the "begining-mid"
                        seeds.append((dstl, seed_src + seed_len - srcl))
                else:
                    # SS
                    pass
            elif seed_src <= srcl + length - 1:
                # 1M
                if seed_src + seed_len - 1 <= srcl + length - 1:
                    # MM
                    pendingseeds.remove(seed)
                    # Transpose it all
                    seeds.append((dstl + seed_src - srcl, seed_len))
                else:
                    # MG
                    pendingseeds.remove(seed)
                    # Add back the "tail"
                    pendingseeds.append(
                        (srcl+length, seed_src+seed_len - (srcl+length)))
                    # Transpose the "mid-end"
                    seeds.append(
                        (dstl+seed_src-srcl, length - seed_src + srcl))
            else:
                # 1G => GG
                pass
        oldseeds = pendingseeds
        l += 1
    seeds += oldseeds
    # pprint(seeds)
    print(len(seeds))
    l += 1
print(min([s[0] for s in seeds if s[1] > 0]))
