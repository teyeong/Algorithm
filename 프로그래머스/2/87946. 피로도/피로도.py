import itertools

def solution(k, dungeons):
    answer = -1
    
    cases = itertools.permutations(dungeons, len(dungeons))

    
    for case in cases:
        curr = k
        cnt = 0
        for val in case:
            if curr >= val[0]:
                cnt += 1
                curr -= val[1]
        answer = max(answer, cnt)
    
    return answer