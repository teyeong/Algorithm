import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    
    res = 0
    
    for a in range(i - 1, x):
        res += sum(arr[a][j - 1:y])
    
    print(res)