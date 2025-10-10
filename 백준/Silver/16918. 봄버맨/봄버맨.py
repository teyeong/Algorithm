import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C, N = map(int, input().split())
grid = [list(input()) for _ in range(R)]

def fill_bomb(grid):
    bomb = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                bomb.append((i, j))
            else:
                grid[i][j] = 'O'
    return grid, bomb

def explode_bomb(grid, bomb):
    for idx, val in enumerate(bomb):
        grid[val[0]][val[1]] = '.'
        for i in range(4):
            nx = val[0] + dx[i]
            ny = val[1] + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                grid[nx][ny] = '.'
    return grid

if N < 2:
    for i in range(R):
        for j in range(C):
            print(grid[i][j], end='')
        print()
    exit()
elif N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print('O', end='')
        print()
    exit()

bomb = []
for i in range(2, N + 1):
    
    if i % 2 == 0:
        # 폭탄 채우기
        grid, bomb = fill_bomb(grid)
    else:
        # 폭탄 터지기
        grid = explode_bomb(grid, bomb)

for i in range(R):
    for j in range(C):
        print(grid[i][j], end='')
    print()