def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    
    for i in range(len(numbers)):
        curr = numbers[i]
        
        while stack and numbers[stack[-1]] < curr:
            answer[stack.pop()] = curr
            
        stack.append(i)
            
    return answer
