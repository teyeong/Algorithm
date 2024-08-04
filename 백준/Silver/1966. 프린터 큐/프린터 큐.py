import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    priority = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append((i, priority[i]))
    order = 0
    for j in range(N):
        while q[0][1] != max(priority):
            q.append(q.pop(0))
        order += 1
        idx, max_p = q.pop(0)
        priority.remove(max_p)
        if idx == M:
            break

    print(order)