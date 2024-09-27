def solution(board):
    height = len(board)
    width = len(board[0])
    dp = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            if board[i][j]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    
    answer = max(max(row) for row in dp) ** 2

    return answer