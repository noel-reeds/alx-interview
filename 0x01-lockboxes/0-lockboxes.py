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
    open_boxes = boxes[0]
    for box in boxes[1:]:
        if box in open_boxes:
            open_boxes.append(key for key in box and key not in open_boxes)
