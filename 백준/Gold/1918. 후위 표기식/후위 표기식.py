priority = { "(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2 }

def infix_to_postfix(exp):
    result = ""
    stack = []
    
    for c in exp:
        if c in priority:
            if c == "(":
                stack.append(c)
            elif c == ")":
                while stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            else: # +, -, *, /
                # 스택에 있는 연산자의 우선 순위가 더 크거나 같으면 출력
                while len(stack) > 0 and priority[c] <= priority[stack[-1]]:
                    result += stack.pop()
                stack.append(c)
        else:
            result += c
    
    while stack:
        result += stack.pop()
    
    return result

exp = input()
print(infix_to_postfix(exp))