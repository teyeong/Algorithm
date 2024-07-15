import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
        
    for i in range(4):
        curr_x = x + dx[i]
        curr_y = y + dy[i]
        
        if curr_x < 0 or curr_x >= R or curr_y < 0 or curr_y >= C:
            continue
        
        if visited[ord(board[curr_x][curr_y]) - 65] == 0:
            # 백트래킹
            visited[ord(board[curr_x][curr_y]) - 65] = 1
            dfs(curr_x, curr_y, cnt + 1)
            visited[ord(board[curr_x][curr_y]) - 65] = 0

board = []
ans = 1

R, C = map(int, input().split())

for _ in range(R):
    board.append(list(input()))

visited = [0] * 26
visited[ord(board[0][0]) - 65] = 1

dfs(0, 0, ans)
print(ans)