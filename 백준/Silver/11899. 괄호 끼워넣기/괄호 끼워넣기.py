import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []

cnt = 0

for ch in S:
    if ch == '(':
        stack.append(ch)
    else:
        if stack:
            stack.pop()
        else:
            cnt += 1

cnt += len(stack)
print(cnt)