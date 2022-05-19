#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    n = len(arr)
    mid = n//2

    if ( n%2 == 1 ):
        return arr[mid]
    else:
        return (arr[mid-1]+arr[mid])//2


def quartiles(arr):
    # Write your code here
    arr.sort()
    # n is last index rather than the length
    n = len(arr)-1
    mid = n//2
    result = []

    if ( n%2 == 0 ):
        result.append(median(arr[:mid]))
        result.append(arr[mid])
        result.append(median(arr[mid+1:]))
    else:
        result.append(median(arr[:mid+1]))
        result.append((arr[mid+1]+arr[mid])//2)
        result.append(median(arr[mid+1:]))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
