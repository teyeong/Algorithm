def solution(board, moves):
    answer = 0
    
    basket = []
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1]:
                if basket and basket[-1] == board[j][moves[i] - 1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
    
    return answer