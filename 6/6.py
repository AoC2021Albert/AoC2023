#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re

# f = open("6/sample.raw", "r")
f = open("6/in.raw", "r")
res = 1
# for time, distance in [(7,9),(15,40),(30,200)]:
# for time, distance in [(61,430),(67,1036),(75,1307),(71,1150)]:
for time, distance in [(61677571, 430103613071150)]:
    win = 0
    for t in range(1, time+1):
        speed = t
        d = speed*(time-t)
        if d > distance:
            win += 1
    res *= win

print(res)
