#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    # arr.sort()
    n = len(arr)
    mean = sum(arr)/n
    arrSum = 0
    
    for ele in arr:
        t = abs(ele - mean)
        arrSum += t*t
    print(round(math.sqrt(arrSum/n),1))

    
if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)
