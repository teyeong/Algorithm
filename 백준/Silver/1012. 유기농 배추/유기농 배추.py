T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = [(x, y)]
    field[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            curr_x = x + dx[i]
            curr_y = y + dy[i]
            
            if curr_x < 0 or curr_x >= M or curr_y < 0 or curr_y >= N:
                # 범위 초과
                continue
            
            if field[curr_x][curr_y] == 1:
                queue.append((curr_x, curr_y))
                field[curr_x][curr_y] = 0

for i in range(T):
    M, N, K = map(int, input().split())
    
    field = [[0] * (N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1
    
    
    for a in range(M):
        for b in range(N):
            if field[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)