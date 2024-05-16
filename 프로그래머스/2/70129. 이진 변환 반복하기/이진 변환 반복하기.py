def solution(s):
    answer = []
    cnt_0 = 0
    cnt_change = 0
    
    while len(s) > 1:
        cnt_0 += s.count('0')
        s = s.replace('0', '')
        s = format((len(s)), 'b')
        cnt_change += 1
        
    answer.append(cnt_change)
    answer.append(cnt_0)
    
    return answer