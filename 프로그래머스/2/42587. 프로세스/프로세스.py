def solution(priorities, location):
    answer = 0
    
    max_priority = max(priorities)
    
    while priorities:
        curr = priorities.pop(0)
        if curr == max_priority:
            answer += 1
            if location == 0:
                break
            else:
                max_priority = max(priorities)
                location -= 1
        else:
            priorities.append(curr)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return answer