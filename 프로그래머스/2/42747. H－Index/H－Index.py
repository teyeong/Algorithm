def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    h = 0 # 최대 h
    for i, val in enumerate(citations):
        if val >= i + 1:
            h = i + 1
        
    return h