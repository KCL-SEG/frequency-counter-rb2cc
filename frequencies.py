from collections import Counter

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    b = []
    # Your code goes here
    if len(items) != 0:
        for i in items:
            b.append(str(i))
        frequencies = Counter(b)
        return frequencies
    else:
        return frequencies
