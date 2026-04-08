from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

pos = 50
ans = 0

for line in stdin:
    direc,  moves = line[0], int(line[1:])
    
    if direc == 'L':
        moves = -moves
    
    pos = (pos + moves)%100
    if pos == 0:
        ans += 1
    print(pos)

print(ans)
