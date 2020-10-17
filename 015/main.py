"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

import random


def foo(s):
    re = None

    for i, j in enumerate(s):
        if random.randint(1, i + 1) == 1:
            re = j
    return re
