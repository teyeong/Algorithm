import sys
input = sys.stdin.readline

N = int(input())

tower = list(map(int, input().split()))

stack = []
ans = [0] * len(tower)

for i, t in enumerate(tower):
    while stack:
        if stack[-1][1] > tower[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append([i, t])
    
print(' '.join(map(str, ans)))