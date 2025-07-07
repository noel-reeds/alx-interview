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
    for box in boxes:
        for keys in boxes[box]:
            # check if box not in opened boxes
            open_boxes.append(boxes[box][keys] not in open_boxes)
            # next box to append to opened boxes
            index = boxes[box][keys]
            next_box = boxes[index]
            open_boxes.append(key for key in next_box and key not open_boxes)

