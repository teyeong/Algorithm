def find_nge(N, A):
    stack = []
    res = [-1] * N
    for i in range(N - 1, -1, -1):
        while stack:
            if stack[-1] > A[i]:
                res[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(A[i])
    return res

N = int(input())
A = list(map(int, input().split()))
res = find_nge(N, A)
res = " ".join(map(str, res))
print(res)