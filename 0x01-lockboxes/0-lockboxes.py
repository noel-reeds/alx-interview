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
    open_boxes = [0]
    for box in range(len(boxes)):
        if box in open_boxes:
            # append keys in current box
            open_boxes.extend([m for m in boxes[box] if m not in open_boxes])
            for keys in range(len(boxes[box])):
                m = boxes[box][keys]
                # append keys in subsequent boxes
                open_boxes.extend([x for x in boxes[m] if x not in open_boxes])
    # check opened boxes against all boxes
    res = all(m in open_boxes for m in range(len(boxes)))
    return res
