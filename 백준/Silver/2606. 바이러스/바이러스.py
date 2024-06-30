from collections import deque

com = int(input())
connect = int(input())
network = [[] for i in range(com + 1)]
visited = [0] * (com + 1)

for _ in range(connect):
    com1, com2 = map(int, input().split())
    network[com1] += [com2]
    network[com2] += [com1]

visited[1] = 1
queue = deque([1])

while queue:
    curr = queue.popleft()
    for nxt in network[curr]:
        if visited[nxt] == 0:
            queue.append(nxt)
            visited[nxt] = 1

print(sum(visited) - 1)