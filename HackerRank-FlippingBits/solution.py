#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    bit_32 = format(n, '032b')
    bit_list = list(bit_32)
    li = []
    for num in bit_list:
        if num == str(0):
            x = str(1)
            li.append(x)
        elif num == str(1):
            x = str(0)
            li.append(x)
        else:
            pass
    li = ''.join(li)
    li = int(li, 2)
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
