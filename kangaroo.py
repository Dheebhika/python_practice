import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    count = 0
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        for i in range(0, 4):
            if x1 + v1 == x2 + v2:
                count += 1


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
