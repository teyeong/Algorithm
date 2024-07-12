def dfs(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return
    for j in range(1, N + 1):
        if j >= arr[cnt - 1]:
            arr[cnt] = j
            dfs(cnt + 1)

arr = [0 for i in range(9)]

N, M = map(int, input().split())

dfs(0)