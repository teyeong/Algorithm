import sys
input = sys.stdin.readline

# 세로 N, 가로 M
N, M = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(N)]

global max_result
max_result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def dfs(x, y, depth, total):
    global max_result
    
    if depth == 4:
        max_result = max(max_result, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + numbers[nx][ny])
                visited[nx][ny] = False

t_shapes = [
    [(-1, 0), (0, -1), (0, 1)],  # ㅗ
    [(1, 0), (0, -1), (0, 1)],   # ㅜ
    [(0, -1), (-1, 0), (1, 0)],  # ㅓ
    [(0, 1), (-1, 0), (1, 0)],   # ㅏ
]

# ㅓ, ㅏ, ㅗ, ㅜ 함수
def check(x, y):
    global max_result
    
    for shape in t_shapes:
        try:
            total = numbers[x][y]
            for dx, dy in shape:
                # 범위에 맞지 않은 좌표
                if x + dx < 0 or y + dy < 0:
                    total = 0
                    break
                total += numbers[x + dx][y + dy]
            max_result = max(max_result, total)
        except IndexError:
            continue
        
visited = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, 1, numbers[x][y])
        visited[x][y] = False
        check(x, y)

# 최댓값 출력
print(max_result)