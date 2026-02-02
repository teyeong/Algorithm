import sys
input = sys.stdin.readline

N, C = map(int, input().split())
fields = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**30

visited = [False] * N
min_cost = [INF] * N

# 시작 정점 (0번 밭)
min_cost[0] = 0
total = 0

for _ in range(N):
    # 아직 방문 안 한 정점 중 최소 비용 정점 선택
    u = -1
    best = INF
    for i in range(N):
        if not visited[i] and min_cost[i] < best:
            best = min_cost[i]
            u = i

    # 더 이상 연결 불가
    if u == -1 or best < C and best != 0:
        print(-1)
        sys.exit(0)

    visited[u] = True
    total += best

    # 다른 정점들의 최소 연결 비용 갱신
    ux, uy = fields[u]
    for v in range(N):
        if not visited[v]:
            vx, vy = fields[v]
            cost = (ux - vx) ** 2 + (uy - vy) ** 2
            if cost >= C and cost < min_cost[v]:
                min_cost[v] = cost

print(total)