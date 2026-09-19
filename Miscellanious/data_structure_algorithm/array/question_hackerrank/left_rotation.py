#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotate_right(arr: list, k: int) -> list:
        if k > len(arr):
            k = k % len(arr)
        elif k == 0 :
            return arr
        
        i = 0
        iswap = -1 * k

        if len(arr) % 2 == 0: #length is even
            #decides the number of times the loop should run
            #based upon the len of arr and k
            check = len(arr) - k if (k <= len(arr)/2) else k
            
            while i < check:
                #swap 
                tmp = arr[i]
                arr[i] = arr[iswap]
                arr[iswap] = tmp
                
                #the condition for iswap values
                iswap += 1 
                if iswap == 0:
                    iswap = -1 * k
                
                i += 1
        else:
            #tells whther k is greater than 
            #half of the length of the array
            #or less than half of the length
            is_greater = True if (k > len(arr)/2) else False
            
            while i < len(arr)-1:
                #swap 
                tmp = arr[i]
                arr[i] = arr[iswap]
                arr[iswap] = tmp
                
                #the condition for iswap values
                if iswap != -1:
                    iswap += 1
                elif not is_greater:
                    iswap = -1*k
                
                i += 1

        return arr

def rotateLeft(d, arr):
    rotate_right(arr, len(arr)-d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
