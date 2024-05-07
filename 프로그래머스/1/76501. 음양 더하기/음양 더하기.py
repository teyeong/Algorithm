def solution(absolutes, signs):
    answer = 0
    
    for i, v in enumerate(signs):
        if v == False:
            absolutes[i] *= -1
        answer += absolutes[i]
    
    return answer