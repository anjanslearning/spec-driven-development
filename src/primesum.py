#!/bin/python3

import os
import sys


def is_prime(value):
    """Return True when value is a prime number."""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False

    limit = int(value**0.5)
    for divisor in range(3, limit + 1, 2):
        if value % divisor == 0:
            return False
    return True


def solve(n, k):
    """Return the sum of all prime numbers in the inclusive range [n, k]."""
    if n > k:
        n, k = k, n

    total = 0
    for number in range(n, k + 1):
        if is_prime(number):
            total += number

    return str(total)


if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH')
    if not output_path:
        output_path = 'output.txt'

    with open(output_path, 'w') as fptr:
        t = int(input().strip())

        for _ in range(t):
            first_multiple_input = input().rstrip().split()
            n = int(first_multiple_input[0])
            k = int(first_multiple_input[1])
            result = solve(n, k)
            fptr.write(result + '\n')
    if output_path == 'output.txt':
        print('Results written to output.txt')
