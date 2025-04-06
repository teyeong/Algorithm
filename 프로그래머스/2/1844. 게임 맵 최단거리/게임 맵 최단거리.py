from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    visit = [[False] * m for _ in range(n)]
    distance = [[False] * m for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((0, 0))
    visit[0][0] = True
    distance[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and maps[nx][ny] == 1:
                    visit[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    
    if distance[n - 1][m - 1] == 0:
        return -1
    return distance[n - 1][m - 1] if not 0 else -1