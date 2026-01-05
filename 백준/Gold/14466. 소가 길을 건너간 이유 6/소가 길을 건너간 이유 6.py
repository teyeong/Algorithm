from itertools import combinations

N, K, R = map(int, input().split())

farm = [[0 for _ in range(N)] for _ in range(N)]
roads = dict()

# 도로 위치 저장
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    if (r1 - 1, c1 - 1) not in roads.keys():
        roads[(r1 - 1, c1 - 1)] = set()
    roads[(r1 - 1, c1 - 1)].add((r2 - 1, c2 - 1))
        
    if (r2 - 1, c2 - 1) not in roads.keys():
        roads[(r2 - 1, c2 - 1)] = set()
    roads[(r2 - 1, c2 - 1)].add((r1 - 1, c1 - 1))

# 소 위치 지정
for i in range(K):
    r, c = map(int, input().split())
    farm[c - 1][r - 1] = i + 1

visited = [[False for _ in range(N)] for _ in range(N)]
answer = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    stack = [(x, y)]
    group = set()
    
    while stack:
        x, y = stack.pop()
        visited[y][x] = True
        
        if farm[y][x] != 0:
            group.add(farm[y][x])
            
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < N:
                if (x, y) in roads.keys() and (nx, ny) in roads[(x, y)]:
                    continue
                if visited[ny][nx]:
                    continue
                
                stack.append((nx, ny))
    answer.append(len(group))

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(x, y)

# 조합
comb = list(combinations(answer, 2))
ans = 0

for c in comb:
    ans += c[0] * c[1]

print(ans)