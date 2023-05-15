#!/usr/bin/python3
"""
Write a meethod that determines if a given data set represents a valid UTF-8 encoding.
* Return: True if data is a valid UTF-8 encoding, else return False
"""


def validUTF8(data):
    """ UTF-8 Validation """
    bytesLong = 0
    binaryMoveLeft7 = 1 << 7
    binaryMoveLeft6 = 1 << 6
    for byte in data:
        binaryMove = 1 << 7
        if bytesLong == 0:
            while byte & binaryMove:
                bytesLong += 1
                binaryMove = binaryMove >> 1
            if bytesLong == 0:
                continue
            if bytesLong == 1 or bytesLong > 4:
                return False
        else:
            if not (byte & binaryMoveLeft7 and not (byte & binaryMoveLeft6)):
                return False
        bytesLong -= 1
    if bytesLong == 0:
        return True
    return False

