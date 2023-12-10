#!/usr/bin/env python
from pprint import pprint

f = open("10/in.raw", "r")
lines = f.read().splitlines()


def printmap(lines):
    for pipemapl in lines:
        print("".join(pipemapl))

# Find starting position (aka 'S', s_pos)
i = 0
s_pos = -1
while s_pos == -1:
    s_pos = lines[i].find('S')
    i += 1
s_pos = (i-1, s_pos)

# Now find one neighbourgh pointing towards us
pos = s_pos
# Up
if lines[s_pos[0]-1][s_pos[1]] in "7F|":
    pos = (s_pos[0]-1, s_pos[1])
    direction = 0
# Right
elif lines[s_pos[0]][s_pos[1]+1] in "-J7":
    pos = (s_pos[0], s_pos[1]+1)
    direction = 1
# Down
elif lines[s_pos[0]+1][s_pos[1]] in "|LJ":
    pos = (s_pos[0]+1, s_pos[1])
    direction = 2
# No need to look Left, as we are guaranteed to have 2 neighbourghs pointing at us
step = 1
# What we have now and will maintain while advancing is:
# pos: the position we are at now (we start with one pointing at 'S')
# direction: the direction we have moved from S to here
#            1:up, 2:right, 3:down, 4:left
# step: The amount of steps taken, so far 1

# We preserve the initial position and direction we take after 'S' as we will use it later
first_pos = pos
first_direction = direction

# We will need info for each step depending on direction and pipe-shape.
# The 5-tuple is (Y-inc,X-inc,NewDirection,ClockwiseCalc,(ClockwiseInner,ClockwiseOuter))
D = [
    # up
    {'|': (-1, 0, 0, 0,
           ([(0, 1)], [(0, -1)])),
     'F': (0, 1, 1, 1,
           ([(1, 1)], [(-1, -1), (0, -1), (-1, 0)])),
     '7': (0, -1, 3, -1,
           ([(-1, 1), (0, 1), (-1, 0)], [(1, -1)]))},
    # right
    {'-': (0, 1, 1, 0,
           ([(1, 0)], [(-1, 0)])),
     '7': (1, 0, 2, 1,
           ([(1, -1)], [(-1, 1), (0, 1), (-1, 0)])),
     'J': (-1, 0, 0, -1,
           ([(1, 1), (0, 1), (1, 0)], [(-1, -1)]))},
    # down
    {'|': (1, 0, 2, 0,
           ([(0, -1)], [(0, 1)])),
     'J': (0, -1, 3, 1,
           ([(-1, -1)], [(1, 1), (0, 1), (1, 0)])),
     'L': (0, 1, 1, -1,
           ([(1, -1), (0, -1), (1, 0)], [(-1, 1)]))},
    # left
    {'-': (0, -1, 3, 0,
           ([(-1, 0)], [(1, 0)])),
     'L': (-1, 0, 0, 1,
           ([(-1, 1)], [(1, -1), (0, -1), (1, 0)])),
     'F': (1, 0, 2, -1,
           ([(-1, -1), (0, -1), (-1, 0)], [(1, 1)]))}
]

# On pipemap we will "draw" our loop only, the rest will be "#"
pipemap = [['#']*len(lines[0]) for _ in range(len(lines))]
pipemap[s_pos[0]][s_pos[1]] = 'S'
# clock will tell us if the loop is clockwise or counterclockwise
clock = 0
while pos != s_pos:
    pipemap[pos[0]][pos[1]] = lines[pos[0]][pos[1]]
    DATA = D[direction][lines[pos[0]][pos[1]]]
    clock += DATA[3]
    new_pos = (pos[0]+DATA[0],
               pos[1]+DATA[1])
    direction = DATA[2]
    pos = new_pos
    step += 1
# Verify our "clock" calculation, it has to be 4 for clockwise and -4 for counterclockwise
if clock == 4:
    clockwise = True
elif clock == -4:
    clockwise = False
else:
    print('FAIL')
    exit()
print(f'The loop has {step} steps')
print(f'Part 1 answer: {step/2}')
print(f'The loop moves {"clockwise" if clockwise else "counterclockwise"}')


# Part 2
# We will follow the loop again, but now only considering the map with our loop and '#'
# We will also expand it with one extra '#' column at left and right
lines = [["#"]+pml+["#"] for pml in pipemap]
# And one extra '#' line at the top and bottom
lines = [["#"]*len(lines[0])]+lines+[["#"]*len(lines[0])]

# Now we recover the first move that we preserved to start looping
# Be aware that things have shifted 1 row and 1 column due to the new '#' border
pos = (first_pos[0]+1, first_pos[1]+1)
s_pos = (s_pos[0]+1, s_pos[1]+1)
direction = first_direction
while pos != s_pos:
    DATA = D[direction][lines[pos[0]][pos[1]]]
    if clockwise:
        IN = DATA[4][0]
        OUT = DATA[4][1]
    else:
        IN = DATA[4][1]
        OUT = DATA[4][0]
    for is_in in IN:
        v = lines[pos[0]+is_in[0]][pos[1]+is_in[1]]
        if v == "#":
            lines[pos[0]+is_in[0]][pos[1]+is_in[1]] = 'I'
        elif v == "O":
            print('FAIL')
            exit()
    for is_out in OUT:
        v = lines[pos[0]+is_out[0]][pos[1]+is_out[1]]
        if v == "#":
            lines[pos[0]+is_out[0]][pos[1]+is_out[1]] = 'O'
        elif v == "I":
            printmap(lines)
            print('FAIL')
            pprint(pos)
            exit()
    new_pos = (pos[0]+DATA[0],
               pos[1]+DATA[1])
    direction = DATA[2]
    pos = new_pos

# count I's
res = 0
for line in lines:
    strline = "".join(line)
    # Fill "inner big spaces"
    while strline.find('I#') != -1:
        ini = strline.find('I#')
        end = strline.find('#I')
        strline = strline[:ini]+'I'*(end-ini+2)+strline[end+2:]
    res += strline.count('I')
    #print(strline, strline.count('I'), res)
print(f'Part 2 answer: {res} positions are interior')