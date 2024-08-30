import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    
    money = 0
    
    while len(files) > 1:
        temp = heapq.heappop(files) + heapq.heappop(files)
        files.append(temp)
        money += temp

    print(money)