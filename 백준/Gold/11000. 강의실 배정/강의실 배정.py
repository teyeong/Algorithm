import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[0], x[1]))
timeq = deque(time)

cnt = []

heapq.heappush(cnt, timeq.popleft()[1])

while timeq:
    lec = timeq.popleft()
    end = heapq.heappop(cnt)
    if lec[0] < end:
        heapq.heappush(cnt, end)
    heapq.heappush(cnt, lec[1])
print(len(cnt))