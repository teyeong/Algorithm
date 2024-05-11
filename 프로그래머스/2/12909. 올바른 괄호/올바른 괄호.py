def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif len(stack) > 0:
            stack.pop()
        else:
            answer = False
            break
    
    if len(stack) != 0:
        answer = False

    return answer