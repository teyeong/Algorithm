def dfs(queen, n, row):
    cnt = 0
    
    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i] - queen[row]) == row - i:
                break
        else:
            cnt += dfs(queen, n, row + 1)
    return cnt

def solution(n):
    queen = [0] * n
    
    return dfs(queen, n, 0)