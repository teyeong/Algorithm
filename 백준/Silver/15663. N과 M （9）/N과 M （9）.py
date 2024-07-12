def dfs(cnt):
    if cnt == M:
        for i in range(M):
            print(new_arr[i], end=" ")
        print()
        return
    check = 0
    for j in range(N):
        if not visit[j] and check != arr[j]:
            visit[j] = 1
            check = new_arr[cnt] = arr[j]
            dfs(cnt + 1)
            visit[j] = 0

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

visit = [0 for _ in range(N)]
new_arr = [0 for _ in range(N)]

dfs(0)