#!/usr/bin/python3
"""Returns a list of lists of integers rep a Pascals Tri"""


def pascal_triangle(n):
    """Pascals Triangle function definition"""
    # n represents number of rows in a triangle
    # return an empty list if n <= 0
    if n <= 0:
        return []
    else:
        # create a list of lists and append inner lists
        list_of_lists = []
        for row in range(n):
            # create inner lists and append elements
            index = 0
            inner_list = []
            while index <= row:
                if index == 0 or index == row:
                    # first or last element of the row
                    inner_list.append(1)
                else:
                    # rest of the elements
                    prev_list = list_of_lists[row - 1]
                    num1 = prev_list[index - 1]
                    num2 = prev_list[index]
                    co_num = num1 + num2
                    inner_list.append(co_num)
                index = index + 1
            list_of_lists.append(inner_list)
        return list_of_lists
