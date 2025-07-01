#!/usr/bin/python3
"""Returns a list of lists of integers rep a Pascals Tri"""

def pascal_triangle(n):
    # n represents number of rows in a triangle
    # return an empty list if n <= 0
    if n <= 0:
        return []
    else:
        # create a list of lists and append inner lists
        pascals_triangle = []
        for row in range(n):
            # create inner lists and append elements
            m = 0
            inner_list = []
            while m < row:
                if m == 0 or m == n:
                    inner_list.append(1)
                else:
                    pass
