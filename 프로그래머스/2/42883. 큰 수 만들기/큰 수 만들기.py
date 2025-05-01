def solution(number, k):    
    # 현재 수가 앞 수보다 크면 앞 수를 지운다
    stack = []
    
    length = len(number) - k
    
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        if len(stack) < length:
            stack.append(n)
    
    return ''.join(stack)