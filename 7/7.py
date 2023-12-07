#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re

#f = open("7/sample.raw", "r")
f = open("7/in.raw", "r")
lines = f.read().splitlines()

#seeds = set(map(int, lines[0].split(': ')[1].split(' ')))
CARDVALUE={
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T':9,
    '9':8,
    '8':7,
    '7':6,
    '6':5,
    '5':4,
    '4':3,
    '3':2,
    '2':1
}
res = 0
hands = []
for l, line in enumerate(lines):
    hand, bid = line.split(' ')
    hand  = list(hand)
    equals = defaultdict(int)
    cardvalues = 0
    for card in hand:
        cardvalues = CARDVALUE[card] + cardvalues * 14
        equals[card]+=1
#    handvalue = cardvalues
    repetitionstring = [str(v) for v in sorted(equals.values(),reverse=True)]
#    for k, v in equals.items():
#        handvalue += (pow(14*14*14*14*14*14,v))
    hands.append((repetitionstring, cardvalues, bid,hand,cardvalues,equals))
hands.sort()
lhands = len(hands)
for i, bid in enumerate([h[2] for h in hands]):
    print(f'adding ${int(bid)} with weigth ${lhands-i}')
    res+=int(bid)*(i+1)


pprint(hands)

print(res)

