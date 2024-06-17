import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort(reverse=True)
max_len = -1
for i in range(len(arr) - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        max_len = sum(arr[i:i+3])
        break
print(max_len)