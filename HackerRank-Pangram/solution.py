#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # get all alphabets i
    characters = list(map(chr, range(97, 123)))
    
    # lowercase the string to avoid double counting
    s = s.lower()
    
    # turn the string into a set to get unique values
    ss = set(s)
    
    # get count of unique values in string and remove blank space char
    s_unique = len(ss)-1
    
    if s_unique == len(characters):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
