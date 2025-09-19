def solution(survey, choices):
    answer = ''
    
    result = [{'R': 0, 'T': 0}, {'C': 0, 'F': 0}, {'J': 0, 'M': 0}, {'A': 0, 'N': 0}]
    
    for i, s in enumerate(survey):
        left = s[0]
        right = s[1]
        
        idx = 0
        for k in range(4):
            if left in result[k].keys():
                idx = k
                break
        
        if choices[i] > 4:
            result[k][right] += choices[i] - 4
        elif choices[i] < 4:
            result[k][left] += 4 - choices[i]
    
    for item in result:
        r = sorted(item.items(), key=lambda x: (-x[1], x[0]))
        answer += r[0][0]
    
    return answer