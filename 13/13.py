#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("13/in.raw", "r")
#f = open("13/sample.raw", "r")
lines = f.read().splitlines()


def solve1(lineset):
    for i in range(1,len(lineset)):
        if lineset[i]== lineset[i-1]:
            #candidate found
            mirror = True
            j=i-2
            k=i+1
            while j>=0 and k<len(lineset):
                mirror = mirror and (lineset[j]==lineset[k])
                j-=1
                k+=1
            if mirror:
                return(100*i)
    # No horiz ref, look vert
    for i in range(1,len(lineset[0])):
        if ''.join([l[i] for l in lineset]) == ''.join([l[i-1] for l in lineset]):
            #candidate found
            mirror = True
            j=i-2
            k=i+1
            while j>=0 and k<len(lineset[0]):
                mirror = mirror and (''.join([l[j] for l in lineset]) == ''.join([l[k] for l in lineset]))
                j-=1
                k+=1
            if mirror:
                return(i)
    print('FAIL')
    exit()


def fix_smudge(by_row, rowset):
    pprint(by_row)
    for candidate in range(1,len(rowset)):
        discrepances=0
        j=candidate-1
        k=candidate
        while j>=0 and k<len(rowset):
            if rowset[j]!=rowset[k]:
                smudge=k
                discrepances+=1
            j-=1
            k+=1
        if discrepances==1:
            s=sum([1 if rowset[smudge][i]!=rowset[smudge-(smudge-candidate)*2-1][i] else 0 for i in range(len(rowset[0]))])
            if s==1:
                return(candidate)
    return(0)

def solve2(lineset):
    by_row = defaultdict(list)
    for i, line in enumerate(lineset):
        by_row[line].append(i)
    if s := fix_smudge(by_row, lineset):
        return(s*100)
    # No horiz ref, look vert
    by_col = defaultdict(list)
    colset=[]
    for i in range(len(lineset[0])):
        col=''.join([l[i] for l in lineset])
        by_col[col].append(i)
        colset.append(col)
    if s := fix_smudge(by_col, colset):
        return(s)
    return(0)
    #print('FAIL')
    #exit()


res = 0
res2=0

lineset=[]
for i, line in enumerate(lines):
    if not line:
        s=solve1(lineset)
        #print(s)
        res+=s
        q=solve2(lineset)
        #print(q)
        res2+=q
        lineset=[]
        print()
    else:
        lineset.append(line)
s=solve1(lineset)
#print(s)
res+=s
q=solve2(lineset)
#print(q)
res2+=q

print(res)
print(res2)