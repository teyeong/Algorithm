def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for i in s:
        if i == 'P' or i == 'p':
            p_cnt += 1
        if i == 'Y' or i == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False