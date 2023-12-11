#!/usr/bin/env python

def star_distances(map, EXPANSE):
    col_offsets = []
    row_offsets = []
    empty_cols = [True] * len(map[0])
    row_offset = 0
    # Scan de map row by row
    for y, row in enumerate(map):
        row_offsets.append(row_offset)
        # If no stars in row
        if row.find('#') == -1:
            # Add EXPANSE offset to subsequent rows
            row_offset += EXPANSE
        # Detect Columns that have stars on this row
        for x, c in enumerate(row):
            if c == '#':
                empty_cols[x] = False

    col_offset = 0
    # For each column
    for x, is_empty in enumerate(empty_cols):
        col_offsets.append(col_offset)
        if is_empty:
            # Add EXPANSE offset to subsecuent columns
            col_offset += EXPANSE

    # With offsetcols and offsetrows ready
    # find real position of stars
    stars = []
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if row[x] == '#':
                stars.append((y + row_offsets[y],
                              x + col_offsets[x]))

    ret = 0
    # The distance is the X-distance + Y-distance
    # For each star
    for i, star in enumerate(stars):
        # Check distance to subsequent stars
        for j in range(i + 1, len(stars)):
            ret += abs(star[0] - stars[j][0])
            ret += abs(star[1] - stars[j][1])

    return (ret)


f = open("11/in.raw", "r")
# f = open("11/sample.raw", "r")
lines = f.read().splitlines()

print(f'Part 1: {star_distances(lines,1)}')
print(f'Part 2: {star_distances(lines,999999)}')
