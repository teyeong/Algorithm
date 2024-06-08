def solution(s):
    answer = 0
    list_s = list(s)
    for i in range(len(list_s)):
        cnt = 0
        stack = []
        for j in list_s:
            if j == '[' or j == '{' or j == '(':
                stack.append(j)
                cnt += 1
            if stack:
                if j == ']' and stack[-1] == '[':
                    stack.pop()
                    cnt += 1
                if j == '}' and stack[-1] == '{':
                    stack.pop()
                    cnt += 1
                if j == ')' and stack[-1] == '(':
                    stack.pop()
                    cnt += 1
        if len(stack) == 0 and len(list_s) == cnt :
            answer += 1
        temp = list_s.pop(0)
        list_s.append(temp)
        
    return answer