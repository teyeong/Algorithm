import sys

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in trees:
        if i > mid:
            total += (i - mid)
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)