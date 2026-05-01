from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

nums = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        nums.append(line.split())

ops = nums[-1]
nums = nums[:-1]

ans = 0

for j in range(len(nums[0])):
    if ops[j] == '+':
        for i in range(len(nums)):
            ans += int(nums[i][j])
    else:
        curr = 1
        for i in range(len(nums)):
            curr *= int(nums[i][j])
        ans += curr


print(ans)
