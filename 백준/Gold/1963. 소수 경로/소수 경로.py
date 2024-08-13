import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

n = 10000
a = [False, False] + [True] * (n - 1)

for i in range(2, n + 1):
  if a[i]:
    for j in range(2 * i, n + 1, i):
        a[j] = False

def bfs():
    q = deque()
    q.append([start, 0])
    
    visit = [0 for _ in range(n)]
    visit[start] = 1
    
    while q:
        now, cnt = q.popleft()
        str_now = str(now)
        
        if now == end:
            return cnt
        
        for i in range(4):
            for j in range(10):
                temp = int(str_now[:i] + str(j) + str_now[i + 1:])
                
                if visit[temp] == 0 and a[temp] and temp > 1000:
                    visit[temp] = 1
                    q.append([temp, cnt + 1])

for _ in range(T):
    start, end = map(int, input().split())
    
    cnt = 0
    
    res = bfs()
    print(res if res != None else "Impossible")