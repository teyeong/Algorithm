def dfs(conn, n):
    cnt = []
    stack = []
    visit = [False] * (n + 1)
    curr_cnt = 0
    
    for i in range(1, n + 1):
        curr_cnt = 0
        if not visit[i]:
            stack.append(i)
            visit[i] = True
            curr_cnt += 1
            while stack:
                curr = stack.pop()
                for j in conn[curr]:
                    if not visit[j]:
                        stack.append(j)
                        visit[j] = True
                        curr_cnt += 1
            cnt.append(curr_cnt)
    return cnt

def solution(n, wires):
    answer = n
    
    connections = [[] for _ in range(n + 1)]
    
    # 송전탑 연결하기
    for v in wires:
        connections[v[0]] += [v[1]]
        connections[v[1]] += [v[0]]
    
    # bfs로 연결된 경우마다 끊어서 최소값 찾기
    for v in wires:
        connections[v[0]].remove(v[1])
        connections[v[1]].remove(v[0])
        cnt = dfs(connections, n)
        answer = min(answer, abs(cnt[0] - cnt[1]))
        connections[v[0]] += [v[1]]
        connections[v[1]] += [v[0]]
        
    return answer