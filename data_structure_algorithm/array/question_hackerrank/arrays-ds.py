#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    left, right = 0, -1
    while left <= len(arr)/2:
        tmp = a[left]
        a[left] = a[right]
        a[right] = tmp
        
        left += 1
        right -= 1
    
    return a
    

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)
