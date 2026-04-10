from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        jolt = 0
        mx = int(int(line[0]))

        for i in range(1, len(line)):
            curr = int(line[i])
            jolt = max(jolt, mx * 10 + curr)
            mx = max(mx, curr)

        ans += jolt



print(ans)
