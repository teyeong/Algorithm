import math

def solution(progresses, speeds):
    answer = []
    
    length = len(speeds)
    
    deploy = [0 for _ in range(length)]
    
    for i in range(length):
        left = 100 - progresses[i]
        days = math.ceil(left / speeds[i])
        deploy[i] = days
    
    curr = deploy[0]
    cnt = 1
    j = 1
    while j < length:
        if curr >= deploy[j]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            curr = deploy[j]
        j += 1
    
    # 마지막 배포
    answer.append(cnt)
    
    return answer