from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0

def getmod(n):
    if len(str(n))%2 == 1:
        return 99999999999999999
    return int(pow(10, len(str(n))//2)+1)

with open("input.txt", "r") as file:
    for line in file:
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')

            for i in range(int(start), int(end)+1):
                if i % getmod(i) == 0:
                    ans += i


print(ans)
