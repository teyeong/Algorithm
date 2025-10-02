import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())

title = []
title_set = set()

for _ in range(N):
    t, num = input().split()
    num = int(num)
    if num not in title_set:
        title.append((t, num))
        title_set.add(num)

for _ in range(M):
    power = int(input())
    
    left, right = 0, len(title) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if power <= title[mid][1]:
            right = mid
        elif power > title[mid][1]:
            left = mid + 1
    
    print(title[right][0])