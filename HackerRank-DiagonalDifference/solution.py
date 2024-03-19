#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    
    point_l = 0
    l_to_r = []
    r_to_l = []
    point_r_1 = n
    point_r_2 = 0
    
    while (point_l < n):
        a = arr[point_l][point_l]
        l_to_r.append(a)
        point_l = point_l+1
    sum_l = (sum(l_to_r))
    
    while (point_r_1 > 0):
        b = arr[point_r_1-1][point_r_2]
        r_to_l.append(b)
        point_r_1 = point_r_1 - 1
        point_r_2 = point_r_2 + 1
    sum_r = (sum(r_to_l))
        
    diff = sum_l - sum_r
    
    if diff < 0:
        diff = diff * -1
    
    return diff
    
    
    

    
        
   
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
