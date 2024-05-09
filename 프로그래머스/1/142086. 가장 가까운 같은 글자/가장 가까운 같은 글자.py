def solution(s):
    answer = []
    letter = []
    letter_idx = []
    
    for i, v in enumerate(s):
        if v in letter:
            idx = letter.index(v)
            answer.append(i - letter_idx[idx])
            letter_idx.insert(idx, i)
            letter_idx.pop(idx + 1)
        else:
            letter.append(v)
            letter_idx.append(i)
            answer.append(-1)
        
    
    return answer