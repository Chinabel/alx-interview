#!/usr/bin/python3
"""
Script to unlock list of lists
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    n = len(boxes)
    myList = [0]
    for i in myList:
        for j in boxes[i]:
            if j not in myList:
                if j < n:
                    myList.append(j)
    if len(myList) == n:
        return True
    return False
