import sys

def bfs(n):
    global cnt
    cnt += 1
    queue = [n]
    visited[n] = 1
    
    while queue:
        curr = queue.pop(0)
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                queue.append(nxt)
                visited[nxt] = 1

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [0] * (N + 1)

# 그래프
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

cnt = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)

print(cnt)