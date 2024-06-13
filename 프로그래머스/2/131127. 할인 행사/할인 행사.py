def solution(want, number, discount):
    answer = 0
    curr_item = []
    curr_cnt = []
    
    for i in range(9):
        if discount[i] in curr_item:
            idx = curr_item.index(discount[i])
            curr_cnt[idx] += 1
        else:
            curr_item.append(discount[i])
            curr_cnt.append(1)
    
    for i in range(9, len(discount)):
        if discount[i] in curr_item:
            idx = curr_item.index(discount[i])
            curr_cnt[idx] += 1
        else:
            curr_item.append(discount[i])
            curr_cnt.append(1)
        
        for j in range(len(want)):
            if want[j] in curr_item:
                idx = curr_item.index(want[j])
                if curr_cnt[idx] != number[j]:
                    break
                if j == len(want) - 1:
                    answer += 1
            else:
                break
        
        idx = curr_item.index(discount[i - 9])
        if curr_cnt[idx] == 1:
            curr_cnt.pop(idx)
            curr_item.pop(idx)
        else:
            curr_cnt[idx] -= 1
    
    return answer