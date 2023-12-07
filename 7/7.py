#!/usr/bin/env python

from collections import defaultdict

f = open("7/in.raw", "r")
lines = f.read().splitlines()

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

def solve(joker_card):
    res = 0
    hands = []
    for line in lines:
        hand, bid = line.split(' ')
        jokers = 0                 # How many jokers in our hand?
        repeats = defaultdict(int) # Repetitions keyed by card
        # card_values will be a base14 value of the hand cards (no "type")
        card_values = 0
        for card in hand:
            if card==joker_card:
                jokers+=1
                card_values = 0 + card_values * 14
            else:
                card_values = CARDVALUE[card] + card_values * 14
                repeats[card]+=1
        # repetition_list is a sorted list of how many of a kind
        # for example "full house" will be [3,2]
        # this allows for natural ordering of "types"
        repetition_list = [v for v in sorted(repeats.values(),reverse=True)]
        # Joker calculations
        if len(repetition_list)==0:
            repetition_list = [5] # 5 jokers
        else:
            repetition_list[0]+=jokers
        # The two first elements of the tuple will now contain
        # the natural ordering of the hands
        # The third element is there to retrieve at the end
        hands.append((repetition_list, card_values, bid))
    hands.sort()
    # We can now calculate the winnings
    for i, bid in enumerate([h[2] for h in hands]):
        res+=int(bid)*(i+1)
    return(res)

print(solve(''))
print(solve('J'))
