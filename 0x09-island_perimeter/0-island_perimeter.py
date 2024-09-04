#!/usr/bin/python3
"""returns the perimeter of the island"""


def island_perimeter(grid):
    """function def"""
    count = [0] * len(grid[0])
    for row in grid:
        for index, cols in enumerate(row):
            if cols != 0:
                count[index] += 1
    height = max(count)
    count2 = []
    for row in grid:
        count = 0
        for cols in row:
            if cols != 0:
                count += 1
        count2.append(count)
    width = max(count2)
    perimeter = 2*(height + width)
    return perimeter
