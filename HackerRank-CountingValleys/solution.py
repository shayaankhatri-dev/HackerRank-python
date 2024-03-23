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
    # Write your code here
    count = 0
    count_list = []
    first_step = path[0]
    count_valley = []
    
    for i in range(len(path)):
        if path[i] == 'D':
            count = count -1
            count_list.append(count)
        elif path[i] == 'U':
            count = count + 1
            count_list.append(count)
        else:
            pass
    
    if first_step == 'D':
        count_valley.append(1)

    for j in range(len(count_list)-1):
        if count_list[j] == 0:
            if count_list[j+1] == -1:
                count_valley.append(1)
                
    return sum(count_valley)
    
   
            
  
        
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
