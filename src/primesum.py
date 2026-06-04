#!/bin/python3

import math
import os
import random
import re
import sys



def solve(n, k):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(result + '\n')

    fptr.close()
