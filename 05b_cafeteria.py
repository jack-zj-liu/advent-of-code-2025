from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
ranges = []
ids = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == '':
            break

        start, end = line.split('-')
        ranges.append([int(start), int(end)])\

    for line in file:
        i = int(line.strip())
        ids.append(i)

ranges.sort()
merged_ranges = []

for s, e in ranges:
    if not merged_ranges or s > merged_ranges[-1][1] + 1:
        merged_ranges.append([s, e])
    else:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], e)

for s, e in merged_ranges:
    ans += e-s+1

print(ans)
