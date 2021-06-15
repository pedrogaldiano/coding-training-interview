#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    relative_to_sea = 0

    for i in range(steps):
        if path[i] == 'D':
            relative_to_sea -= 1
        elif path[i] == 'U':
            relative_to_sea += 1

        if relative_to_sea == 0 and path[i] == 'U':
            valleys += 1
    return valleys
    
print(countingValleys(8, 'UDDDUDUU'))