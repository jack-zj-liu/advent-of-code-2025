from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0

mods = {2: [11],
        3: [111],
        4: [1111, 101],
        5: [11111],
        6: [111111, 10101, 1001],
        7: [1111111],
        8: [11111111, 10001, 1010101],
        9: [111111111, 1001001],
        10: [1111111111, 100001, 101010101]
}

with open("input.txt", "r") as file:
    for line in file:
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')

            for i in range(int(start), int(end)+1):
                if len(str(i)) not in mods:
                    continue

                for m in mods[len(str(i))]:
                    if i%m == 0:
                        ans += i
                        print(i)
                        break

# 6,812,585,188
print(ans)
