T = int(input())

for _ in range(T):
    PS = input()
    
    stack = []
    flag = 0
    
    for ch in PS:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                flag = 1
                break
    
    if stack:
        flag = 1
    
    if flag:
        print("NO")
    else:
        print("YES")