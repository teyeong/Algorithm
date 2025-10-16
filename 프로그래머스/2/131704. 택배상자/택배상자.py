def solution(order):
    answer = 0    
    sub_container = [] # stack
    ord_idx = 0 # order 리스트의 인덱스
    
    flag = False
    for i in range(1, len(order) + 1):
        flag = False
        if ord_idx < len(order):
            while (order[ord_idx] == i) or (len(sub_container) > 0 and sub_container[-1] == order[ord_idx]):
                if order[ord_idx] == i:
                    flag = True
                if len(sub_container) > 0 and sub_container[-1] == order[ord_idx]:
                    sub_container.pop()
                ord_idx += 1
                answer += 1
                if ord_idx >= len(order):
                    break
            if not flag:
                sub_container.append(i)
        else:
            break
    
    return answer