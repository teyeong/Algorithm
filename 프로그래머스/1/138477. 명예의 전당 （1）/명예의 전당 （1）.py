def solution(k, score):
    answer = []
    rank = []
    
    for i, v in enumerate(score):
        if len(rank) < k:
            rank.append(v)
        elif rank[0] < v:
            rank.pop(0)
            rank.append(v)
        rank.sort()
        answer.append(rank[0])
    
    return answer