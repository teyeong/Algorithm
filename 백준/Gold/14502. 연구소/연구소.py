import sys
input = sys.stdin.readline
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    q = []
    q.append(start)
    while q:
        curr = q.pop(0)
        for i in range(4):
            x = curr[0] + dx[i]
            y = curr[1] + dy[i]
            
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            
            if temp_map[x][y] == 0:
                temp_map[x][y] = 2
                q.append([x, y])

N, M = map(int, input().split())

road_map = []

max_result = 0
starts = []

for i in range(N):
    road_map.append(list(map(int, input().split())))
    
    for j in range(M):
        if road_map[i][j] == 2:
            starts.append([i, j])

num = [0] * (N * M)
for i in range(N * M):
    num[i] = i

comb = list(combinations(num, 3)) # 3개 벽 조합
for val in comb:
    line1 = val[0] // M
    seq1 = val[0] % M
    
    line2 = val[1] // M
    seq2 = val[1] % M
    
    line3 = val[2] // M
    seq3 = val[2] % M
    
    if road_map[line1][seq1] != 0 or road_map[line2][seq2] != 0 or road_map[line3][seq3] != 0:
        continue
    
    temp_map = copy.deepcopy(road_map)
    
    temp_map[line1][seq1] = 1
    temp_map[line2][seq2] = 1
    temp_map[line3][seq3] = 1
    
    for start in starts:
        bfs(start)
    
    cnt = 0
    for i in range(N):
        cnt += temp_map[i].count(0)
    max_result = max(max_result, cnt)

print(max_result)