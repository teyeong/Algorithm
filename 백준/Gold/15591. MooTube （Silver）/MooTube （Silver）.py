from collections import deque

N, Q = map(int, input().split())

USADO = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    
    USADO[p].append((q, r))
    USADO[q].append((p, r))
    
def bfs(start, k):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    
    # k 이상인 동영상 개수
    cnt = 0
    
    while q:
        curr = q.popleft()
        for nxt, usado in USADO[curr]:
            if not visited[nxt] and usado >= k:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
    return cnt


# 답 구하기
for idx in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))