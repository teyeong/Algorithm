import sys

def find_max(arr):
    res = 0
    best = -10**8
    for num in arr:
        res = max(res + num, num)
        best = max(best, res)
    return best

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

print(find_max(arr))