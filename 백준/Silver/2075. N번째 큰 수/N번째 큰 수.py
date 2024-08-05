import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []

init = list(map(int, input().split()))
for n in init:
    heapq.heappush(heap, n)

for _ in range(N - 1):
    arr = list(map(int, input().split()))
    
    for n in arr:
        if heap[0] < n:
            heapq.heappush(heap, n)
            heapq.heappop(heap)

print(heap[0])