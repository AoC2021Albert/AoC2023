#!/usr/bin/env python
from functools import reduce
from operator import mul
from copy import deepcopy

f = open("19/in.raw", "r")
#f = open("19/sample.raw", "r")
lines = f.read().splitlines()


def bigger(part, category, value):
    return (part[category] > value)


def smaller(part, category, value):
    return (part[category] < value)


# Loading data
processor = {}
i = 0
while line := lines[i]:
    name, rulestring = line.split('{')
    rulestring = rulestring[:-1]
    rules_strings = rulestring.split(',')
    rules = []
    for rule_string in rules_strings[:-1]:
        conds, dest = rule_string.split(':')
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
    i += 1
parts = lines[i+1:]


def process_part(part, processor, total_value):
    step = 'in'
    while step not in ['R', 'A']:
        for rule in processor[step]:
            if rule[1](part, rule[0], rule[2]):
                step = rule[3]
                break
    if step == 'R':
        return (0)
    else:
        return (total_value)


# Part 1
res = 0
for line in parts:
    part = {}
    total_value = 0
    for attrs in line[1:-1].split(','):
        attr, value = attrs.split('=')
        value = int(value)
        part[attr] = value
        total_value += value
    res += process_part(part, processor, total_value)
print(res)


def solve_ranges(step, ranges, processor):
    ranges = deepcopy(ranges)
    if step == 'R':
        return (0)
    if step == 'A':
        return (reduce(mul, [v[1] - v[0] + 1 for v in ranges.values()]))
    ret = 0
    for category, comp, value, dest in processor[step]:
        cat_range = ranges[category]
        if comp == bigger:
            if value < cat_range[0]:
                # applies to all
                ret += (solve_ranges(dest, ranges, processor))
                return (ret)
            elif value >= cat_range[1]:
                # applies to none
                ...
            else:  # split
                ranges[category] = (value + 1, cat_range[1])
                ret += solve_ranges(dest, ranges, processor)
                ranges[category] = (cat_range[0], value)
        else:
            assert (comp == smaller)
            if value > cat_range[1]:
                # applies to all
                ret += (solve_ranges(dest, ranges, processor))
                return (ret)
            elif value <= cat_range[0]:
                # applies to none
                ...
            else:  # split
                ranges[category] = (cat_range[0], value - 1)
                ret += solve_ranges(dest, ranges, processor)
                ranges[category] = (value, cat_range[1])
    print('FAIL')
    exit()


# Part 2
print(
    solve_ranges('in', {'x': (1, 4000),
                        'm': (1, 4000),
                        'a': (1, 4000),
                        's': (1, 4000)}, processor)
)
