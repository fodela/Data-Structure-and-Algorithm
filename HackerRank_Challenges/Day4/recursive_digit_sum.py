"""We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

        super_digit(9875)   	9+8+7+5 = 29 
        super_digit(29) 	2 + 9 = 11
        super_digit(11)		1 + 1 = 2
        super_digit(2)		= 2  
Example


The number  is created by concatenating the string   times so the initial .

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of  sum to . The digits of  sum to .  is only one digit, so it is the super digit.

Function Description

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

string n: a string representation of an integer
int k: the times to concatenate  to make 
Returns

int: the super digit of  repeated  times
Input Format

The first line contains two space separated integers,  and .

Constraints


    """

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n: str, k: int):
    # Write your code here
    digit: str = str(n) * k

    def sum_up(digit: str) -> int:
        global result
        summed_digit = 0
        if len(digit) == 1:
            result = digit
        else:
            summed_digit += sum([str(n) for n in digit])
            sum_up(str(summed_digit))

    sum_up(digit)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
