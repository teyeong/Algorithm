from queue import PriorityQueue
def solution(n, costs):
    connection = [[] for _ in range(n)]
    
    for val in costs:
        island1, island2, cost = val
        connection[island1] += [(cost, island2)]
        connection[island2] += [(cost, island1)]

    visit = [False for _ in range(n)] # 방문 여부 확인
    cost_sum = 0 # 반환 값
    queue = PriorityQueue() # 우선순위 큐
    
    # 0번 섬에서 시작
    for val in connection[0]:
        queue.put(val)
    visit[0] = True
    
    while False in visit:
        curr_cost, island = queue.get()
        if not visit[island]:
            cost_sum += curr_cost
            visit[island] = True
            for val in connection[island]:
                queue.put(val)
    return cost_sum