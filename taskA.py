#!/bin/python3

import math
import os
import random
import re
import sys
import dateutil.parser


def time(t1, t2):

    date1 = dateutil.parser.parse(t1, fuzzy=True)
    date2 = dateutil.parser.parse(t2, fuzzy=True)

    diff = date2 - date1
    return str(int(abs(diff.total_seconds())))

if __name__ == '__main__':
    print("Enter total tests : ")
    t = int(input())
    for t_itr in range(t):
        print("Enter first date :")
        t1 = input()
        print("Enter second date :")
        t2 = input()

        result = time(t1, t2)

        print(result + '\n')
