#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr.sort()
    print(arr[len(arr) - 1])
    brr.sort()
    print(brr[len(brr) - 1])
    array = []
    j = 0
    for i in range(0, len(brr)):
        if j >= len(arr):
            array.append(brr[i])
        elif brr[i] != arr[j]:
            array.append(brr[i])
        else:
            j = j + 1
    print(array)
    value = list(set(array))
    value.sort()
    return value


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)
arr = [204, 205, 206]
brr = [206, 204, 204, 209, 205]

arr.sort()
brr.sort()
array = []
j = 0
for i in range(0, len(brr)):
    if brr[i] != arr[j]:
        array.append(brr[i])
    else:
        if j < len(arr) - 1:
            j = j + 1
result = list(set(array))
result.sort()
print(result)
