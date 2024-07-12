def dfs(cnt):
    if len(new_arr) == M:
        for i in range(M):
            print(new_arr[i], end=" ")
        print()
        return
    check = 0
    for j in range(cnt, N):
        if check != arr[j]:
            check = arr[j]
            new_arr.append(arr[j])
            dfs(j)
            new_arr.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

new_arr = []

dfs(0)