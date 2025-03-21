from collections import deque

def solution(n, computers):
    answer = 0
    visited = deque([False for _ in range(n)])
    
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    
    return answer

def dfs(n, computers, i, visited):
    visited[i] = True   # 방문 표시
    for j in range(n):
        if j != i and computers[i][j] == 1: # 연결된 경우
            if visited[j] == False: # 방문하지 않은 경우
                dfs(n, computers, j, visited)