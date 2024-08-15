import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    
    if s == '.':
        break
    
    stack = []
    flag = 0
    
    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 1
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 1
                break
    
    if stack:
        flag = 1
        
    if flag:
        print('no')
    else:
        print('yes')