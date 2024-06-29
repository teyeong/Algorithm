N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])
info.sort(key=lambda x: (x[1], x[0]))
idx = 0
cnt = 1
for i in range(1, N):
    if info[idx][1] <= info[i][0]:
        idx = i
        cnt += 1
print(cnt)