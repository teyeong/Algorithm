def solution(t, p):
    answer = 0
    p_len = len(p)
    
    for i, v in enumerate(t):
        if i > len(t) - p_len:
            continue
        new_t = int(t[i:i + p_len])
        if new_t <= int(p):
            answer += 1
    return answer