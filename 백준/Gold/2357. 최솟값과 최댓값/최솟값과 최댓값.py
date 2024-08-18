import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def make_tree(idx, s, e):
    if s == e:
        tree[idx] = (arr[s], arr[s])
        return tree[idx]
    
    mid = (s + e) // 2
    
    l = make_tree(idx * 2, s, mid)
    r = make_tree(idx * 2 + 1, mid + 1, e)
    
    tree[idx] = (min(l[0], r[0]), max(l[1], r[1]))
    return tree[idx]

def search(s, e, idx):
    if e < a or b < s:
        return (10 ** 9 + 1, 0)
    
    if a <= s and e <= b:
        return tree[idx]
    
    mid = (s + e) // 2

    l = search(s, mid, idx * 2)
    r = search(mid + 1, e, idx * 2 + 1)
    
    return (min(l[0], r[0]), max(l[1], r[1]))

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

b = math.ceil(math.log2(N)) + 1
node = 1 << b
tree = [0 for _ in range(node)]
make_tree(1, 0, len(arr) - 1)

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    ans = search(0, len(arr) - 1, 1)
    print(ans[0], ans[1])