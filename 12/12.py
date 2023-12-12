#!/usr/bin/env python
from functools import cache

f = open("12/in.raw", "r")
# f = open("12/sample.raw", "r")
lines = f.read().splitlines()


@cache
def solve(seqs, nums):
    ret = 0
    # Check terminal cases
    if len(seqs) == 0:
        if len(nums) == 0:
            # Valid combo, no seqs and no nums
            return (1)
        else:
            # I have some nums to assign, but no seq to assign to
            return (0)
    if len(nums) == 0:
        if "".join(seqs).find('#') != -1:
            # We found one spring in a seq but no nums left
            return (0)
        else:
            # There are no more springs in seq and no more nums, this is fine
            return (1)
    # Non-terminal case, we have at least a num and a seq
    num = nums[0]
    nums = nums[1:]
    firstseq = seqs[0]
    seqs = seqs[1:]
    # If the num is larger than the seq, we have to discard it (if possible)
    while len(firstseq) < num:
        if len(seqs) == 0:
            # No more seqs remaining, not possible
            return (0)
        if firstseq.find('#') != -1:
            # Discard a seq with a broken spring? not possible
            return (0)
        # All fine, pick next sequence
        firstseq = seqs[0]
        seqs = seqs[1:]
    # Now we have a candidate seq for num with len>=num
    # first we check all ways it can fit
    for discard in range(len(firstseq)-num+1):
        # We check if the seq part we will discard has no broken springs
        if firstseq[:discard].find('#') == -1:
            # We "consume" the discard plus the num
            newfirst = firstseq[discard+num:]
            if newfirst:
                # The seq still continues, it must have a '?' we must discard
                if newfirst[0] == '?':
                    newfirst = newfirst[1:]
                    if newfirst:
                        ret += solve(tuple([newfirst]+list(seqs)), nums)
                    else:
                        ret += solve(seqs, nums)
                else:
                    ...  # We have a broken spring next, not a working one, not possible
            else:
                #we consumed all the seq, we can check solutions with what's left
                ret += solve(seqs, nums)

    # Then we check that IF the seq is "???"s, we discard it
    if firstseq.find('#') == -1:
        ret += solve(seqs, tuple([num]+list(nums)))
    return (ret)


def get_seqs_from_springs(springs):
    seqs = []
    seq = ''
    for c in springs:
        if c == '.':
            if seq:
                seqs.append(seq)
            seq = ''
        else:
            seq += c
    if seq:
        seqs.append(seq)
    return (seqs)


res = 0
res_p2 = 0
for i, line in enumerate(lines):
    springs, nums = line.split(' ')
    nums = tuple(map(int, nums.split(',')))
    seqs = get_seqs_from_springs(springs)
    res += solve(tuple(seqs), nums)

    # part 2
    springs = '?'.join([springs]*5)
    nums = nums*5
    seqs = get_seqs_from_springs(springs)
    res_p2 += solve(tuple(seqs), nums)

print(res)
print(res_p2)
