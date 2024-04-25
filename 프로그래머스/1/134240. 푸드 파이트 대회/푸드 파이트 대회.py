def solution(food):
    answer = ''
    
    for i in range(1, len(food)): # 앞 선수
        for j in range(food[i] // 2):
            answer += str(i)
    
    answer += '0' # 물 마시기
    
    for i in range(len(food) - 1, 0, -1): # 뒷 선수
        for j in range(food[i] // 2):
            answer += str(i)
            
    return answer