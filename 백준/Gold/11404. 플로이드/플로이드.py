import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
 
city = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
 
for _ in range(m):
    a, b, c = map(int, input().split())
    if city[a][b] > c:
        city[a][b] = c

# 시작 도시 == 도착 도시
for i in range(1, n + 1):
    city[i][i] = 0

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

# 출력
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if city[r][c] == INF:
            print(0, end=" ")
        else:
            print(city[r][c], end=" ")
    print()