#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    Args: boxes argument is a list of lists
    """
    # check if the first box has keys
    if len(boxes[0]) < 1:
        return False
    # otherwise retrieve keys
    opened = [0]
    for box in range(len(boxes)):
        if box in opened:
            # append keys in current box
            opened.extend([m for m in boxes[box] if m not in opened])
            for keys in range(len(boxes[box])):
                m = boxes[box][keys]
                # check if index m is within range of boxes
                if m < len(boxes):
                    # append keys in subsequent boxes
                    opened.extend([x for x in boxes[m] if x not in opened])
    # check opened boxes against all boxes
    res = all(m in opened for m in range(len(boxes)))
    return res
