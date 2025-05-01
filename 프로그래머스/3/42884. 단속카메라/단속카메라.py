def solution(routes):    
    routes.sort(key=lambda x: x[1])
    
    answer = 1
    idx = 1
    time = routes[0][1]
    
    while idx < len(routes):
        if not routes[idx][0] <= time <= routes[idx][1]:
            answer += 1
            time = routes[idx][1]
        idx += 1
    
    return answer