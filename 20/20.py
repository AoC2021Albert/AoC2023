#!/usr/bin/env python
from collections import defaultdict, deque
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("20/in.raw", "r")
f = open("20/fd-xs.raw", "r")
f = open("20/hm-kl.raw", "r")
f = open("20/jc-ml.raw", "r")
f = open("20/pl-jn.raw", "r")

#f = open("20/sample2.raw", "r")
#f = open("20/sample.raw", "r")
lines = f.read().splitlines()
HIGH, LOW = "^", "V" # as long as they are different...
OFF, ON = 0, 1

modules={}
srcs = defaultdict(list)

# Process Input
for line in lines:
    left, right = line.split(' -> ')
    kind = left[0]
    name = left[1:]
    dsts = [dst for dst in right.split(', ')]
    for dst in dsts:
        srcs[dst].append(name)
    modules[name] = [kind, OFF, dsts]

for name, module in modules.items():
    kind, state, dsts = module
    if kind == '&':
        module[1] = {src_name:LOW for src_name in srcs[name]}


def button_press():
    counter = { LOW: 0, HIGH: 0}
    rx_low = False
    signals = deque([('button', LOW, ['roadcaster'])])
    while signals:
        signal = signals.popleft()
        sending_name, pulse, receiving_names = signal
        for receiving_name in receiving_names:
            counter[pulse] += 1
            if receiving_name == 'rx' and pulse == LOW:
                rx_low = True
            if receiving_name in modules:
                module = modules[receiving_name]
                kind, state, dsts = module
                if kind == 'b':
                    signals.append((receiving_name, pulse, dsts))
                elif kind == '%':
                    if pulse == LOW:
                        if state == OFF:
                            signals.append((receiving_name, HIGH, dsts))
                            module[1] = ON
                        elif state == ON:
                            signals.append((receiving_name, LOW, dsts))
                            module[1] = OFF
                        else:
                            assert False, 'BAD FF STATE'
                    else:
                        ... # High pulse, ignore
                elif kind == '&':
                    state[sending_name] = pulse
                    if all([remembered==HIGH for remembered in state.values()]):
                        signals.append((receiving_name, LOW, dsts))
                    else:
                        signals.append((receiving_name, HIGH, dsts))
                else:
                    assert False,'BAD KIND'
    return(counter[LOW],counter[HIGH], rx_low)

''' Part 1
res = { LOW: 0, HIGH: 0}
for _ in range(1000):
    pushes = button_press()
    res[LOW]+=pushes[0]
    res[HIGH]+=pushes[1]

print(res[LOW]*res[HIGH])
'''

# Mermaid chart printing
dq = deque(srcs['rx'])
visited = set()
while dq:
    s = dq.popleft()
    if s not in visited:
        visited.add(s)
        print(f'{s}[{modules[s][0]} {s}]')
        for dst in modules[s][2]:
            print(f'{s} --> {dst}')
        dq.extend(srcs[s])
print()
print()

# Solving one section and checking loop size
i = 1
prev_i = 0
iterations = 0
while True:
    pushes = button_press()
    if pushes[2]:
        print(i, i-prev_i)
        prev_i = i
        iterations += 1
        if iterations>10:
            exit()
    i+=1

# The answer to part 2 is the LCM of all 4 "sections"