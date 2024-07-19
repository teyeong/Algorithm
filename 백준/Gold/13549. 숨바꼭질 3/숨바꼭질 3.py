from collections import deque

def bfs():
    q = deque([N])
    visit[N] = 1
    
    while q:
        v = q.popleft()
        vv = 2 * v
        
        if vv <= 100000 and not visit[vv]:
            q.appendleft(vv)
            visit[vv] = visit[v]
        
        for w in [v - 1, v + 1]:
            if 0 <= w <= 100000 and not visit[w]:
                q.append(w)
                visit[w] = visit[v] + 1

N, K = map(int, input().split())
visit = [0 for _ in range(100001)]
bfs()
print(visit[K] - 1)