#!/usr/bin/env python
from collections import deque

f = open("23/in.raw", "r")
# f = open("23/sample.raw", "r")
lines = f.read().splitlines()

SLOPEDIR = (    '^',    '>',    'v',    '<' )
DIRS     = ((-1, 0), (0, 1), (1, 0), (0, -1))

SRC_COORD = (0, 1)
DST_COORD = (len(lines)-1, len(lines[-1])-2)


def solvep1(y, x):
    longest = [[0]*len(lines[0]) for _ in range(len(lines))]
    dq = deque([(y, x, [(y, x)],)])
    while dq:
        y, x, path = dq.popleft()
        if y >= len(lines)-1:
            longest[len(lines)-2][len(lines[0]) -
                                  1] = max(longest[len(lines)-2][len(lines[0])-1], len(path))
        elif y <= 0 or longest[y][x] >= len(path) or (y, x) in path[:-1]:
            ...  # don't follow this path...
        else:
            longest[y][x] = len(path)
            for d in range(4):
                yinc, xinc = DIRS[d]
                ny, nx = y + yinc, x + xinc
                if lines[ny][nx] == '.':
                    dq.append((ny, nx, path + [(ny, nx)]))
                elif lines[ny][nx] == SLOPEDIR[d]:
                    assert lines[ny+yinc][nx+xinc] == '.'
                    dq.append((ny+yinc, nx+xinc, path +
                              [(ny, nx), (ny+yinc, nx+xinc)]))
    return(longest[len(lines)-2][len(lines[0])-1])


def get_dests(lines):
    '''
    Returns a dict where
    key: coordiantes of a fork
    value: list of tuples with 2 objects:
         0: coordinates of other fork
         1: stpes needed to reach that other fork
    '''
    def get_all_forks(lines):
        '''
        Returns a dict where
        key: coordiantes of a fork
        value: list of directions this fork exits
        '''
        forks = {SRC_COORD: [2],
                 DST_COORD: [0]}
        # Check all the inner maze for forks
        for y in range(1, len(lines)-1):
            for x in range(1, len(lines[0])-1):
                if lines[y][x] != '#':
                    dirs = []
                    for d in range(4):
                        yinc, xinc = DIRS[d]
                        if lines[y+yinc][x+xinc] != '#':
                            dirs.append(d)
                    if len(dirs) > 2:
                        forks[(y, x)] = dirs
                    else:
                        # All non-forks must have 2 exits (no cul-de-sacs)
                        assert len(dirs) == 2
                        # We could accomodate to cul-de-sacs by adding them as forks
                        # We would add them with an empty "dirs",
                        # as we would not want to waste time on them
        return (forks)

    dests = {}
    forks = get_all_forks(lines)
    for fork in forks:
        y, x = fork
        dirs = forks[fork]
        dest = []
        for d in dirs:
            dist = 1
            ny, nx = y, x
            yinc, xinc = DIRS[d]
            nd = (d - 1) % 4
            while (ny+yinc, nx+xinc) not in forks.keys():
                ny += yinc
                nx += xinc
                while lines[ny+DIRS[nd][0]][nx+DIRS[nd][1]] == '#':
                    nd = (nd+1) % 4
                yinc, xinc = DIRS[nd]
                nd = (nd - 1) % 4
                dist += 1
            dest.append(((ny+yinc, nx+xinc), dist))
        dests[fork] = dest
    return (dests)

def find_longest_path(fork, dst_fork, dests, path, pathlen, longest_path):
    if fork in path:
        return (longest_path)
    else:
        path.append(fork)
        if fork == dst_fork:
            longest_path = max(longest_path, pathlen)
        else:
            for subfork, dist in dests[fork]:
                longest_path = max(longest_path, find_longest_path(
                    subfork, dst_fork, dests, path, pathlen+dist, longest_path))
        path.pop()
    return (longest_path)


# Part 1
print(solvep1(1, 1))

# Part 2
print(find_longest_path(SRC_COORD, DST_COORD, get_dests(lines), [], 0, 0))
