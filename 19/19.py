#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("19/in.raw", "r")
#f = open("19/sample.raw", "r")
lines = f.read().splitlines()


def bigger(part, category, value):
    return(part[category]> value)

def smaller(part, category, value):
    return(part[category]< value)

processor = {}
i = 0
while line := lines[i]:
    name, rulestring = line.split('{')
    rulestring=rulestring[:-1]
    rules_strings=rulestring.split(',')
    rules=[]
    for rule_string in rules_strings[:-1]:
        conds,dest=rule_string.split(':')
        if '>' in conds:
            category, value = conds.split('>')
            value = int(value)
            rules.append((category, bigger, value, dest))
        else:
            category, value = conds.split('<')
            value = int(value)
            rules.append((category, smaller, value, dest))
    rules.append(('x', bigger, -9999999, rules_strings[-1]))
    processor[name] = rules
    i+=1


def process(part, processor, total_value):
    step = 'in'
    while step not in ['R', 'A']:
        for rule in processor[step]:
            if rule[1](part,rule[0],rule[2]):
                step = rule[3]
                break
    if step == 'R':
        return(0)
    else:
        return(total_value)



res = 0
i+=1

while i < len(lines):
    line = lines[i][1:-1]
    part = {}
    total_value = 0
    for attrs in line.split(','):
        attr, value = attrs.split('=')
        value = int(value)
        part[attr] = value
        total_value += value
    res += process(part, processor, total_value)
    i+=1

print(res)
