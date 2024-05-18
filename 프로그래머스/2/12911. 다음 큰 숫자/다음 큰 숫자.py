def solution(n):
    answer = n + 1
    
    binary_n = format(n, 'b')
    cnt_1 = binary_n.count('1')
    
    while True:
        binary_ans = format(answer, 'b')
        cnt_ans = binary_ans.count('1')
        if cnt_ans == cnt_1:
            break
        else:
            answer += 1
    
    return answer