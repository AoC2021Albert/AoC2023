#!/usr/bin/env python
f = open("11/in.raw", "r")
# f = open("11/sample.raw", "r")
lines = f.read().splitlines()

EXPANSE = 999999


def star_distance(map, EXPANSE):
    X_SIZE = len(map[0])
    Y_SIZE = len(map)
    offsetcols = [0] * X_SIZE
    offsetrows = [0] * Y_SIZE
    emptycols = [True] * X_SIZE
    # Scan de map row by row
    for y, row in enumerate(map):
        # If no stars in row
        if row.find('#') == -1:
            # Add EXPANSE offset to subsequent rows
            for i in range(y + 1, Y_SIZE):
                offsetrows[i] += EXPANSE
        # Detect Columns that have stars on this row
        for x, c in enumerate(row):
            if c == '#':
                emptycols[x] = False

    # For each column
    for x, is_empty in enumerate(emptycols):
        if is_empty:
            # Add EXPANSE offset to subsecuent columns
            for i in range(x + 1, X_SIZE):
                offsetcols[i] += EXPANSE

    # With offsetcols and offsetrows ready
    # find real position of stars
    stars = []
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if row[x] == '#':
                stars.append((y + offsetrows[y],
                              x + offsetcols[x]))

    distance_sum = 0
    # The distance is the X-distance + Y-distance
    # For each star
    for i, star in enumerate(stars):
        # Check distance to subsequent stars
        for j in range(i + 1, len(stars)):
            distance_sum += abs(star[0] - stars[j][0])
            distance_sum += abs(star[1] - stars[j][1])

    return (distance_sum)

print(f'Part 1: {star_distance(lines,1)}')
print(f'Part 2: {star_distance(lines,999999)}')
