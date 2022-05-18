#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    n = len(arr)
    mid = n//2
    if ( n%2 == 1 ):
        return arr[mid]
    else:
        return (arr[mid-1]+arr[mid])/2


def interQuartile(values, freqs):
    arr = []
    for i in range(len(freqs)):
        arr.extend([values[i]]*freqs[i])
    arr.sort()
    
    n = len(arr)
    mid = n//2
    
    if ( n%2 == 0 ):
        print(round(median(arr[mid:]) - median(arr[:mid]),1))
    else:
        print(round(median(arr[mid+1:]) - median(arr[:mid]),1))


if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)