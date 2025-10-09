import sys
input = sys.stdin.readline
import itertools

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
corridor = [list(input().split()) for _ in range(N)]

pos_X = []
pos_T = []

for x in range(N):
    for y in range(N):
        if corridor[x][y] == 'X':
            pos_X.append((x, y))
        elif corridor[x][y] == 'T':
            pos_T.append((x, y))

def trace(cor):
    for i in range(len(pos_T)):
        x, y = pos_T[i]
        for j in range(4):
            cx, cy = x, y
            while True:
                nx = cx + dx[j]
                ny = cy + dy[j]
                
                if 0 <= nx < N and 0 <= ny < N:
                    if cor[nx][ny] == 'S':
                        return False
                    elif cor[nx][ny] == 'T' or cor[nx][ny] == 'O':
                        break
                else:
                    break
                
                cx, cy = nx, ny
    return True

flag = False
comb = list(itertools.combinations(pos_X, 3))

for idx, val in enumerate(comb):
    corridor[val[0][0]][val[0][1]] = 'O'
    corridor[val[1][0]][val[1][1]] = 'O'
    corridor[val[2][0]][val[2][1]] = 'O'
    
    flag = trace(corridor)
    if flag == True:
        print('YES')
        exit()
    
    corridor[val[0][0]][val[0][1]] = 'X'
    corridor[val[1][0]][val[1][1]] = 'X'
    corridor[val[2][0]][val[2][1]] = 'X'
    
print('NO')