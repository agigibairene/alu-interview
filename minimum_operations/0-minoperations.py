#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """Calculates the number of operations to result n H characters"""
    min_operations = 0

    if n <= 1:
        return min_operations

    for i in range(2, n + 1):
        while n % i == 0:
            min_operations += i
            n /= i
    return min_operations
