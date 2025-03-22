def solution(clothes):
    answer = 1
    comb = {}
    
    for item, name in clothes:
        if name in comb.keys():
            comb[name].append(item)
        else:
            comb[name] = [item]
    
    for _, item in comb.items():
        answer *= len(item) + 1
        
    return answer - 1