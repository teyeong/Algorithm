def solution(name):
    answer = 0
    
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    min_move = len(name) - 1
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        distance = min(i * 2 + len(name) - next_i, (len(name) - next_i) * 2 + i)
        min_move = min(min_move, distance)
    
    answer += min_move
    
    return answer