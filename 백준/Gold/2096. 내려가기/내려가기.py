import sys
input = sys.stdin.readline
import math

N = int(input())

find_max = [0, 0, 0]
find_min = [0, 0, 0]

for _ in range(N):
    line = list(map(int, input().split()))
    find_max = [line[0] + max(find_max[:2]), line[1] + max(find_max), line[2] + max(find_max[1:])]
    find_min = [line[0] + min(find_min[:2]), line[1] + min(find_min), line[2] + min(find_min[1:])]
    

print(max(find_max), min(find_min))