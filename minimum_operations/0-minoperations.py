#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the number of operations to result n H characters"""
    if (n < 2):
        return 0

    min_Operation = 0

  
    for i in range(2, (n + 1)):

        while (n % i == 0):
            min_Operation += i
            n //= i

    return min_Operation
