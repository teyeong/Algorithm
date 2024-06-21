def cal2(q):
    first = q.pop(0)
    q.append(first)

def cal3(q):
    last = q.pop()
    q.insert(0, last)
    
N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = [j for j in range(1, N + 1)]
cnt = 0

for idx in range(M):
    while arr[idx] != q[0]:
        curr = q.index(arr[idx])
        if curr <= len(q) // 2:
            cal2(q)
        else:
            cal3(q)
        cnt += 1
    q.pop(0)

print(cnt)