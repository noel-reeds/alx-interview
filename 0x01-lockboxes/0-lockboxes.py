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
    # otherwise retrieve keys and open the rest of the boxes
