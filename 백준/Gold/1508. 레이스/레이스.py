N, M, K = map(int, input().split())
pos = list(map(int, input().split()))

left = 0
right = N
D = 0

candidates = [] # 가장 가까운 두 심판의 거리가 될 수 있는 후보군

while left <= right: # 이분 탐색
    D = (left + right) // 2
    cnt = 1
    prev = 0
    for nxt in range(1, K):
        if pos[nxt] - pos[prev] >= D:
            cnt += 1
            prev = nxt
    
    if cnt >= M:
        candidates.append(D)
        left = D + 1
    else:
        right = D - 1

candidates.sort()
D = candidates[-1] # 가장 가까운 두 심판의 거리: 최대 거리

cnt = 1
prev = 0
idx = set([0])
for nxt in range(1, K):
    if cnt == M:
        break
    if pos[nxt] - pos[prev] >= D:
        cnt += 1
        prev = nxt
        idx.add(nxt)

ans = ''
ans_cnt = 0
for i in range(K):
    if i in idx:
       ans_cnt += 1
       ans += '1'
    else:
        ans += '0'

print(ans)