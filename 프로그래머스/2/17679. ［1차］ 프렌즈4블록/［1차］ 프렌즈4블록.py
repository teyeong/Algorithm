dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 우, 하, 대각선
pos_x = [1, 0, 1]
pos_y = [0, 1, 1]

# 빈 공간을 채우는 함수
def fill_blank(m, n, board):
    for y in range(n):
        blocks = []
        for x in range(m):
            if board[x][y] != '@':
                blocks.append(board[x][y])
                board[x][y] = '@'
        for i in range(len(blocks)):
            board[m - i - 1][y] = blocks[len(blocks) - i - 1]
    
    return board
    
def remove_block(board, positions):
    for position in positions:
        board[position[0]][position[1]] = '@'
    
    return board
    
    
# 각 블록별 4칸 확인 함수
def bfs(m, n, board):
    visit = [[False for _ in range(n)] for _ in range(m)]
    lst_pos = []
    
    for i in range(m):
        for j in range(n):
            if not visit[i][j] and 65 <= ord(board[i][j]) <= 90:
                visit[i][j] = True
                flag = True
                tmp_pos = [(i, j)]
                
                for idx in range(3):
                    x = i + pos_x[idx]
                    y = j + pos_y[idx]
                    
                    if 0 <= x < m and 0 <= y < n:          
                        if board[i][j] != board[x][y]:
                            flag = False
                            break
                        else:                           
                            tmp_pos.append((x, y))

                    else:
                        flag = False
                        break
                
                if flag:
                    lst_pos += tmp_pos

    set_pos = set(lst_pos)
    board = remove_block(board, set_pos)
    
    res = True if len(set_pos) > 0 else False
    
    return res, board, len(set_pos)
                
def solution(m, n, board):
    answer = 0
    
    # 리스트화
    board = [list(row) for row in board]
    
    flag, board, cnt = bfs(m, n, board)
                       
    while flag:
        board = fill_blank(m, n, board)
        answer += cnt
        
        flag, board, cnt = bfs(m, n, board)
    
    return answer