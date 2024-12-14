#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    MOD = 1234567
    result = 1
    for route in routes:
        result = (result * route) % MOD
    return result

# Input reading and processing
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of towns
    routes = list(map(int, input().split()))  # Routes between towns
    print(connectingTowns(n, routes))
