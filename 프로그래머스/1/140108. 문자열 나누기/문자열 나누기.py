def solution(s):
    answer = 0
    x_cnt = 0
    not_x_cnt = 0
    
    for i in s:
        if x_cnt == not_x_cnt:
            answer += 1
            k = i
        if k == i:
            x_cnt += 1
        else:
            not_x_cnt += 1
    
    return answer