import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    comm, a, b = map(int, input().split())
    if comm:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)