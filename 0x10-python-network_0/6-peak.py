#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers."""
    if not list_of_integers:
        return None

    def recursive_search(li, a, b):
        m = (a + b) // 2

        # Single element or peak at the boundaries
        if a == b:
            return li[a]
        if a + 1 == b:
            return li[a] if li[a] >= li[b] else li[b]

        # Middle element check
        if (m == 0 or li[m] >= li[m - 1]) and (m == b or li[m] >= li[m + 1]):
            return li[m]

        # Recursively search in the half where a larger neighbor is
        if m > 0 and li[m - 1] > li[m]:
            return recursive_search(li, a, m - 1)
        else:
            return recursive_search(li, m + 1, b)

    return recursive_search(list_of_integers, 0, len(list_of_integers) - 1)
